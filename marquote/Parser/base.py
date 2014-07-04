
class Parser():
    sentences = []

    def get_next(self):
        for sentence in self.sentences:
            yield sentence

    def __len__(self):
        return len(self.sentences)


class Sentence():
    def __init__(self, text, char):
        self.text = text
        self.char = char


class ProgressBar():
    def __init__(self, length, name="Progress", width=50):
        self.bar = "[" + " "*width + "] 0%"
        self.name = name
        self.print_name = name + ":" + " "*8
        self.length = length
        self.width = width

    def update(self, new_length):
        percent = int(100 * new_length / self.length)
        marked = int(percent * self.width / 100)
        self.bar = self.print_name
        self.bar += "[" + "=" * marked + " " * (self.width - marked) + "] "
        self.bar += str(percent) + "%"

        print("\r" + self.bar, end="")


