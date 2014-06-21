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

                if char.find('[') != -1:
                    char = char[:char.find('[') - 1]

                text = line[line.find(':') + 2:]

                if text[0] == '(':
                    text = text[text.find(')') + 2:]

                if text[-1].isalpha():
                    text = text + "."

                text = text.split()

                self.sentences.append(Sentence(text, char))


    def get_next(self):
        for sentence in self.sentences:
            yield sentence

class Sentence():
    def __init__(self, text, char):
        self.text = text
        self.char = char
