from cell import Cell
from random import randint


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
                s += column.__str__()
        return s

    def build_grid(self):
        grid = []
        for _ in range(self.lines):
            inner = []
            grid.append(inner)
            for _ in range(self.cols):
                inner.append(Cell())
        return grid

    def randomize(self):
        for line in self.grid:
            for column in line:
                index = randint(0, 8)
                if index == 8:
                    index = None
                column.set_orientation(index)
