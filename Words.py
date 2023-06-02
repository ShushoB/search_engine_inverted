class Word:
    def __init__(self, input):
        self.input = input
        self.output = ''.join(char.lower() for char in self.input if char.isalpha())

    def __repr__(self):
        return self.output



