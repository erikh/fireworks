from cell import Cell
from firework import Firework
from random import randint


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
        self.add_turtle(Firework(lines, cols))
        self.add_turtle(Firework(lines, cols))
        self.add_turtle(Firework(lines, cols))

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

    # randomizes the orientations of the columns. this is mostly just to test
    # the drawing functions. tick() will be used in typical scenarios in place
    # of this, to allow turtles to draw to the screen.
    def randomize(self):
        for line in self.grid:
            for column in line:
                index = randint(0, 8)
                if index == 8:
                    index = None
                column.set_orientation(index)

    def add_turtle(self, turtle):
        self.turtles.append(turtle)

    def tick(self):
        for turtle in self.turtles:
            turtle.tick(self)
