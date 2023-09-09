from teletype.io import style_format


class Cell:
    OrientationTop = 0
    OrientationTopRight = 1
    OrientationRight = 2
    OrientationBottomRight = 3
    OrientationBottom = 4
    OrientationBottomLeft = 5
    OrientationLeft = 6
    OrientationTopLeft = 7

    orientation = None
    fg = "white"
    bg = ""

    def set_orientation(self, orientation):
        self.orientation = orientation

    def set_fg(self, fg):
        self.fg = fg

    def set_bg(self, bg):
        self.bg = bg

    def char(self):
        match self.orientation:
            case None:
                return " "
            case self.OrientationTop:
                return "|"
            case self.OrientationBottom:
                return "|"
            case self.OrientationLeft:
                return "-"
            case self.OrientationRight:
                return "-"
            case self.OrientationBottomLeft:
                return "/"
            case self.OrientationTopRight:
                return "/"
            case self.OrientationBottomRight:
                return "\\"
            case self.OrientationTopLeft:
                return "\\"
            case _:
                return self.orientation.__str__()

    def __str__(self):
        return style_format(
                "%s" % self.char(),
                "%s %s" % (self.fg, self.bg)
        )
