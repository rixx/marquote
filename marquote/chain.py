

class Chain():

    def __init__(self, backend):
        self.backend = backend

    """ Gets a sentence with a given source and/or character aswell as
        configurable lookahead.

        This basically wraps the get function of the backend. 
        For each sequence of words it sends a request to the backend.
        The words are separated by " " and returned.
        
    """
    def get(self, source, lookahead=3, character=None):
        sentence = [self.backend.SENTENCE_START]

        #TODO: check if lookahead size is alright

        while sentence[-1] != self.backend.SENTENCE_END:
            sentence.append(self.backend.get(sentence[-lookahead:], \
                            source, character))
            
        return " ".join(sentence[1:-1]) + "."

    def parse(self, inputfile, source):
        if not hasattr(self, 'parser'):
            return False

        self.parser.source(inputfile)

        for sentence in self.parser.getnext():
            sentence.text.insert(0, self.backend.SENTENCE_START)
            sentence.text.append(self.backend.SENTENCE_END)

            self.backend.put(sentence.text, source, sentence.char)

