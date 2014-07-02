import re
from marquote.Parser.base import Sentence, Parser

class ShakespeareParser(Parser):
    def source(self, filename, sonnets=False):
        if sonnets:
            self.parse_sonnets(filename)
        else:
            self.parse_plays(filename)

    def parse_play(self, filename):
        pass

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

