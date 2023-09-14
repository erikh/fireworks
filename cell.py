from random import choice


class Cell:
    ExplosionChars = ["*", "'", ".", "`", "#", "^", "@", "$", " "]
    RisingChars = ["|", "^", ".", ",", "*", "$", ")", "(", "\\", "/", " "]

    character = " "
    color = "\x1b[0m"

    def set_empty(self):
        self.character = " "

    def set_rising(self):
        self.character = choice(self.RisingChars)

    def set_explosion(self):
        self.character = choice(self.ExplosionChars)

    def set_character(self, character):
        self.character = character

    def set_color(self, color):
        self.color = color

    def __str__(self):
        return "%s%s\x1b[0m" % (self.color, self.character)
