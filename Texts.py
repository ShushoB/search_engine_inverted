from Words import Word


class Text:
    txt1 = {}
    txt2 = {}

    def __init__(self, path):
        with open(path, 'r') as file:
            self.path = path
            if self.path == "/Users/picsartacademy/Downloads/1.txt" :
                for line in file:
                    for word in line.split():
                        new_word = Word(word)
                        if new_word.output not in Text.txt1:
                            Text.txt1[new_word.output] = 1
                        else:
                            Text.txt1[new_word.output] += 1
            else:
                for line in file:
                    for word in line.split():
                        new_word = Word(word)
                        if new_word.output not in Text.txt2:
                            Text.txt2[new_word.output] = 1
                        else:
                            Text.txt2[new_word.output] += 1

