import Texts


class Search:
    def search(self, target):
        self.target = target
        if self.target in Texts.Text.txt1 and self.target in Texts.Text.txt2 :
            if Texts.Text.txt1[self.target] > Texts.Text.txt2[self.target] :
                print('1.txt', "\n", '2.txt')
            else:
                print('2.txt', "\n", '1.txt')
        elif self.target in Texts.Text.txt1:
            print('1.txt')
        elif self.target in Texts.Text.txt2:
            print('2.txt')
        else:
            self.normalize(self.target)

    def normalize(self, target):
        self.target = target
        if self.target.endswith("ies"):
            self.target = self.target.replace("ies", "y")
            self.search(self.target)
        elif self.target.endswith("s"):
            self.target = self.target.replace("s", "")
            self.search(self.target)
        else:
            print("No results found")

