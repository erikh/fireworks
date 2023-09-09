from teletype.io import style_format
from random import randint

OrientationTop = 0
OrientationTopRight = 1
OrientationRight = 2
OrientationBottomRight = 3
OrientationBottom = 4
OrientationBottomLeft = 5
OrientationLeft = 6
OrientationTopLeft = 7


class Cell:
    orientation = OrientationTop
    fg = "white"
    bg = ""

    def __init__(self, orientation, fg, bg):
        self.orientation = orientation
        self.fg = fg
        self.bg = bg

    def __str__(self):
        return style_format(
                "%s" % ["-", "/", "\\", "|"][randint(0, 3)],
                "%s %s" % (self.fg, self.bg)
        )
