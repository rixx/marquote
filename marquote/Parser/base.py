
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
    def __init__(self, length, name="Progress", width=50, done=False):
        self.bar = "[" + " "*width + "] 0%"
        self.value = 0
        self.name = name
        self.print_name = name + ":" + " "*8
        self.length = length
        self.width = width

    def update(self, new_length=None, done=False, detail=True):
        if not new_length:
            new_length = self.value + 1

        if new_length > self.length:
            new_length = self.length

        self.value = new_length

        percent = int(100 * new_length / self.length)
        marked = int(percent * self.width / 100)
        self.bar = self.print_name
        self.bar += "[" + "=" * marked + " " * (self.width - marked) + "] "

        if not done:
            self.bar += str(percent) + "%"
            if detail:
                self.bar += " (" + str(new_length) + "/" + str(self.length) \
                        + str(")"
        else:
            self.bar += "[DONE]"

        print("\r" + self.bar, end="")

    def done(self):
        self.update(self.length, done=True)
        print("")

