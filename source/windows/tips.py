from random import choice


class Tips:
    def __init__(self):
        self.tips = []

        with open("products/tips.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                self.tips.append(line)

    def new_tip(self):
        return choice(self.tips)
