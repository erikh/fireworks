from color import Color

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
    fg = Color(255, 255, 255)
    bg = Color(0, 0, 0)

    def __init__(self, orientation, fg, bg):
        self.orientation = orientation
        self.fg = fg
        self.bg = bg

    def __str__(self):
        return "Cell(%d, %s, %s)" % (self.orientation, self.fg, self.bg)
