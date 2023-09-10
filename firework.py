from turtle import Turtle
from direction import Direction
from random import randint


class Firework(Turtle):
    MaxIterations = 10

    detonated = False
    trail = 1
    embers = []
    speed = 1
    iterations_since_last_animation = 0

    def __init__(self, lines, cols):
        self.speed = randint(1, 3)
        self.embers = [Direction(
            randint(0, cols), lines, Direction.Up, self.trail
        )]
        self.iterations_since_last_animation = 0

    def draw(self, screen):
        for ember in self.embers:
            ember.draw(screen)

    def update(self):
        if self.detonated:
            return
        else:
            if self.iterations_since_last_animation == self.MaxIterations:
                self.embers[0].spread(self.speed)
                self.trail += self.speed
                self.iterations_since_last_animation = 0
            elif randint(
                    self.iterations_since_last_animation,
                    self.MaxIterations
                    ) == self.MaxIterations:
                self.embers[0].spread(self.speed)
                self.trail += self.speed
                self.iterations_since_last_animation = 0
            else:
                self.iterations_since_last_animation += 1

        return

