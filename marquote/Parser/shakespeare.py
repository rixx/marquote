import re
from marquote.Parser.base import Sentence, Parser

class ShakespeareParser(Parser):
    def source(self, filename, sonnets=False):
        if sonnets:
            self.parse_sonnets(filename)
        else:
            self.parse_plays(filename)

    def parse_plays(self, filename):
        """ parses the plays found on Project Gutenberg """
        temp_char = ""
        remainder = ""

        with open(filename, "r") as f:
            for line in f:
                if self._is_next_character(line):
                    dot = line.find('.')
                    temp_char = line[:dot].strip()
                    remainder = self._parse_play_line(line[dot + 2:], \
                            temp_char, remainder)

                elif self._is_text(line) and temp_char:
                    remainder = self._parse_play_line(line.strip(), \
                            temp_char, remainder)


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

