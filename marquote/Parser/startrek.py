import re
from urllib import request
from bs4 import BeautifulSoup
from marquote.Parser.base import Sentence, Parser

class StarTrekParser(Parser):

    def source(self, url):
        soup = BeautifulSoup(request.urlopen(url))

        for line in soup.get_text().splitlines():
            self._parse_line(line)

    def _parse_line(self, line):
        #nice2have: also parse $person's log entries

        # If the line starts with CHARACTER: text …
        # (otherwise, it's irrelevant and doesn't need to be parsed)
        colon = line.find(':')

        if colon != -1 and line[0].isalpha() and line[:colon].isupper():
            char = line[:colon].capitalize()
            text = line[colon + 2:]

            # remove "[OC]" and similar from character
            if char.find('[') != -1:
                char = char[:char.find('[') - 1]

            for sentence in re.split('\. |\? |! ', text):
                self._parse_sentence(sentence, char)

    def _parse_sentence(self, sentence, char):
        # remove stage directions
        if sentence:               
            if sentence[0] == '(':
                sentence = sentence[sentence.find(')') + 2:]

        # remove trailing punctuation
        if sentence:
            while re.match('\.|\?|!', sentence[-1]):
                sentence = sentence[:-1]

            sentence = sentence.split()

            if len(sentence) >= 4:
                self.sentences.append(Sentence(sentence, char))

