from turtle import Turtle
from direction import Direction
from random import randint


class Firework(Turtle):
    detonated = False
    trail = 1
    embers = []

    def __init__(self, lines, cols):
        self.embers.append(Direction(
            randint(0, cols), lines, Direction.Up, self.trail
        ))

    def draw(self, screen):
        for ember in self.embers:
            ember.draw(screen)

    def update(self):
        if self.detonated:
            return
        else:
            self.embers[0].spread()
            self.trail += 1
        return

