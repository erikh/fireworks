from cell import Cell, OrientationTop


class Screen:
    grid = []
    lines = 0
    cols = 0

    def __init__(self, lines, cols):
        self.lines = lines
        self.cols = cols
        self.grid = self.build_grid()

    def __str__(self):
        s = ""
        for line in self.grid:
            for column in line:
                s += "%s" % column
        return s

    def build_grid(self):
        return [
                [
                    Cell(
                        OrientationTop,
                        "white",
                        "on-blue"
                    )
                ] * self.cols
        ] * self.lines
