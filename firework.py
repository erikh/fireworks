from turtle import Turtle
from direction import Direction
from random import randint


class Firework(Turtle):
    MaxIterations = 10
    MaxDrawIterations = 20

    detonated = False
    trail = 1
    embers = []
    speed = 1
    total_iterations = 0
    iterations_since_last_animation = 0
    base_x = 0
    lines = 0

    def __init__(self, lines, cols):
        self.speed = randint(1, 3)
        self.base_x = randint(0, cols)
        self.lines = lines
        self.embers = [Direction(
            self.base_x, self.lines, Direction.Up, self.speed, False
        )]
        self.total_iterations = 0
        self.iterations_since_last_animation = 0
        self.max_iterations_before_detonation = \
            (self.lines / self.speed * 0.8 * 2).__ceil__()
        self.is_finished = False

    def create_embers(self):
        embers = []

        for direction in [
                Direction.Up,
                Direction.UpLeft,
                Direction.UpRight,
                Direction.Down,
                Direction.DownLeft,
                Direction.DownRight,
                Direction.Left,
                Direction.Right
                ]:
            embers.append(Direction(
                self.base_x,
                self.lines - self.trail,
                direction,
                randint(1, 10),
                True
            ))
        self.embers = embers
        return

    def finished(self):
        self.is_finished

    def draw(self, screen):
        if self.iterations_since_last_animation < self.MaxDrawIterations:
            for ember in self.embers:
                ember.draw(screen)
        else:
            for ember in self.embers:
                ember.clear(screen)
            self.embers = []
            self.is_finished = True

    def update(self, screen):
        if self.detonated:
            for ember in self.embers:
                ember.spread(self.speed)
                self.iterations_since_last_animation += 1
        elif self.trail < self.lines + self.speed:
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

            if randint(
                    self.total_iterations,
                    self.max_iterations_before_detonation
                    ) == self.max_iterations_before_detonation:
                self.embers[0].clear(screen)
                self.detonated = True
                self.iterations_since_last_animation = 0
                self.create_embers()
        else:
            self.is_finished = True

        return

