import re
from marquote.Parser.base import Sentence, Parser, ProgressBar

class ShakespeareParser(Parser):
    def source(self, filename, sonnets=False):
        if sonnets:
            self.parse_sonnets(filename)
        else:
            self.parse_plays(filename)

    def parse_plays(self, filename):
        """ parses the plays found on 
        http://sydney.edu.au/engineering/it/~matty/Shakespeare/ """
        temp_char = ""
        remainder = []
        empty_line = False
        start = False
        bar = ProgressBar(length=sum(1 for line in open(filename)),\
                name="Parsing " + filename)

        with open(filename, "r") as f:
            for line in f:
                bar.update()

                if not start:
                    if "ACT I" in line:
                        start = True
                else:
                    if not line or line.isspace():
                        empty_line = True

                    else:
                        if empty_line and self._is_next_character(line):
                            tab = line.find('\t')
                            temp_char = line[:tab]
                            remainder = self._parse_play_line(line[tab + 1:], \
                                    temp_char, [])
                        elif temp_char and self._is_text(line):
                            remainder = self._parse_play_line(line.strip(), \
                                    temp_char, remainder)
                        empty_line = False

            bar.done()

    def _is_next_character(self, line):
        if line and line[0].isalpha() and line.find('\t') != -1 \
          and not "SCENE" in line:
            return True
        else:
            return False

    def _is_text(self, line):
        if line[0] == '\t' and len(line) > 1:
            return True
        else:
            return False

    def _parse_play_line(self, text, char, remainder):
        if text[0] == '[':
            text = text[text.find(']') + 1:]
        if text.find(']') != -1:
            return remainder

        sentences = re.split('\. |\? |\! ', text)
        sentences = [sentence.lower().split() for sentence in sentences]
        sentences[0] = remainder + sentences[0]

        if sentences and sentences[0]:
            if re.match('\.|\?|!', sentences[-1][-1][-1]):
                end = len(sentences)
                sentences[-1][-1] = sentences[-1][-1][:-1]
            else:
                end = len(sentences) - 1

            for index in range(end -1, -1, -1):
                self.sentences.append(Sentence(sentences[index], char))
                del sentences[index]

        if sentences:
            return sentences[0]
        else:
            return []

    def parse_sonnets(self, filename):
        """ parses the sonnets found on Project Gutenberg """
        temp_sentence = []
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line.isnumeric():
                    continue

                line = [l.lower for l in line]
                sentences = re.split('\. |\? |! ', line)

                while len(sentences) > 1:
                    temp_sentence.extend(sentences[0].split())
                    self.sentences.append(Sentence(temp_sentence, None))
                    temp_sentence = []
                    del(sentences[0])

                temp_sentence.extend(sentences[0].split())
                if temp_sentence and re.match('\.|\?|!', temp_sentence[-1][-1]):
                    temp_sentence[-1] = temp_sentence[-1][:-1]
                    self.sentences.append(Sentence(temp_sentence, None))
                    temp_sentence = []

