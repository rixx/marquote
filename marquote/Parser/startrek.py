import re
from bs4 import BeautifulSoup
from urllib import request
from marquote.Parser.base import Sentence, Parser

class StarTrekParser(Parser):


    def source(self, url):
        soup = BeautifulSoup(request.urlopen(url))

        for line in soup.get_text().splitlines():
            #nice2have: also parse $person's log entries
            if line.find(':') != -1 \
              and line[0].isalpha() \
              and line[:line.find(':')].isupper():
                char = line[:line.find(':')]
                char = char[0] + char[1:].lower()

                if char.find('[') != -1:
                    char = char[:char.find('[') - 1]

                text = line[line.find(':') + 2:]

                for sentence in re.split('\. |\? |! ', text):
                    if sentence:               

                        if sentence[0] == '(':
                            sentence = sentence[sentence.find(')') + 2:]

                    if sentence:

                        if re.match('\.|\?|!', sentence[-1]):
                            sentence = sentence[:-1]

                        sentence = sentence.replace(',', '')
                        sentence = sentence.split()

                        if len(sentence) >= 4:
                            self.sentences.append(Sentence(sentence, char))



