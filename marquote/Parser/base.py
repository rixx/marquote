
class Parser():
    sentences = []

    def get_next(self):
        for sentence in self.sentences:
            yield sentence

class Sentence():
    def __init__(self, text, char):
        self.text = text
        self.char = char
