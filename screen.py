from cell import Cell
from firework import Firework


class Screen:
    turtles = []
    grid = []
    lines = 0
    cols = 0

    def __init__(self, lines, cols):
        self.lines = lines
        self.cols = cols
        self.grid = self.build_grid()
        self.turtles = []
        for _ in range(10):
            self.add_turtle(Firework(lines-1, cols-1))

    def __str__(self):
        s = ""
        for line in self.grid:
            for column in line:
                s += column.__str__()
            s += "\n"
        return s.strip()

    def build_grid(self):
        grid = []
        for _ in range(self.lines):
            inner = []
            grid.append(inner)
            for _ in range(self.cols):
                inner.append(Cell())
        return grid

    def add_turtle(self, turtle):
        self.turtles.append(turtle)

    def tick(self):
        for turtle in self.turtles:
            turtle.tick(self)
