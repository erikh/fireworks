from teletype.io import style_format
from random import randint


class Cell:
    ExplosionChars = ["*", "'", ".", "`", "#", " "]

    character = " "
    fg = "white"
    bg = ""

    def set_empty(self):
        self.character = " "

    def set_rising(self):
        self.character = "|"

    def set_explosion(self):
        self.character = self.ExplosionChars[
            randint(0, len(self.ExplosionChars)-1)
        ]

    def set_character(self, character):
        self.character = character

    def set_fg(self, fg):
        self.fg = fg

    def set_bg(self, bg):
        self.bg = bg

    def __str__(self):
        return style_format(
            "%s" % self.character,
            "%s %s" % (self.fg, self.bg)
        )
