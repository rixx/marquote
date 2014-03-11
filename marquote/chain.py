

class Chain():

    def __init__(self, backend):
        self.backend = backend

    def get(self, lookahead=3, source, character=None):
        sentence = [self.backend.SENTENCE_START]

        while sentence[-1] != self.backend.SENTENCE_END:
            sentence.append(self.backend.get(sentence[-lookahead:], \
                            source, character))
            
        return " ".join(sentence[1:-1])

    def parse(self, inputfile, source):
        if not hasattr(self, 'parser'):
            return False

        self.parser.source = inputfile

        for sentence in self.parser.getnext():
            sentence.insert(0, self.backend.SENTENCE_START)
            sentence.append(self.backend.SENTENCE_END)

            self.backend.put(sentence, source)

