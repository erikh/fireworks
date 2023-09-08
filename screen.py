from cell import Cell, OrientationTop
from color import Color


class Screen:
    grid = []
    lines = 0
    cols = 0

    def __init__(self, lines, cols):
        self.lines = lines
        self.cols = cols
        self.build_grid()

    def __str__(self):
        s = "[\n"
        for row in self.grid:
            for column in row:
                s += "%s," % column
            s += "\n"
        s += "\n]"
        return s

    def build_grid(self):
        self.grid = [
                [
                    Cell(
                        OrientationTop,
                        Color(255, 255, 255),
                        Color(0, 0, 0)
                    )
                ] * self.cols
        ] * self.lines
