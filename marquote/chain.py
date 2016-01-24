from marquote.Parser.base import ProgressBar


class ChainGenerator():
    parser = None

    def __init__(self, backend):
        self.backend = backend

    """ Gets a sentence with a given source and/or character aswell as
        configurable lookahead.

        This basically wraps the get function of the backend.
        For each sequence of words it sends a request to the backend.
        The words are separated by " " and returned.

    """
    def generate(self, source, lookahead=3, character=None):
        sentence = [self.backend.SENTENCE_START]

        # TODO: check if lookahead size is alright

        while sentence[-1] != self.backend.SENTENCE_END:
            new_word = self.backend.get(sentence[-lookahead:], source, character)
            sentence.append(new_word)

        if sentence[1].islower():
            sentence[1] = sentence[1].capitalize()

        return " ".join(sentence[1:-1]) + "."

    def parse(self, inputfile, source, **kwargs):
        try:
            self.parser.source(inputfile, **kwargs)
        except TypeError:
            return False

        bar = ProgressBar(name="Processing "+inputfile, length=len(self.parser))

        for sentence in self.parser.get_next():
            sentence.text.insert(0, self.backend.SENTENCE_START)
            sentence.text.append(self.backend.SENTENCE_END)

            self.backend.put(sentence.text, source, sentence.char)
            bar.update()

        bar.done()
