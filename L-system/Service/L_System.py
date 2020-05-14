def rule_one():
    return "F+[[X]-X]-F[-FX]+X"


def rule_two():
    return "FF"


class L_System:
    def __init__(self):
        self.word = ["X"]
        self.words = []

    def iterate_replace(self, n):
        new_word = ""
        for i in range(n):
            if i != 0:
                self.word = new_word
                self.words.append(new_word)
            new_word = ""
            for list_item in self.word:
                for letter in list_item:
                    if letter == "X":
                        new_word += rule_one()
                    elif letter == "F":
                        new_word += rule_two()
                    else:
                        new_word += letter
        return self.word



