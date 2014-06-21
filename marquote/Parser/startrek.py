import re
from bs4 import BeautifulSoup
from urllib import request

class StarTrekParser():


    def source(self, url):
        self.sentences = []
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

                        if sentence[-1].isalpha():
                            sentence = sentence + "."

                        sentence = sentence.replace(',', '')
                        sentence = sentence.split()

                        if len(sentence) >= 4:
                            self.sentences.append(Sentence(sentence, char))


    def get_next(self):
        for sentence in self.sentences:
            yield sentence

class Sentence():
    def __init__(self, text, char):
        self.text = text
        self.char = char
