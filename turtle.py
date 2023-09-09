# logo represent

class Turtle:
    directions = []

    def update(self):
        return

    def draw(self, screen):
        return

    def tick(self, screen):
        for direction in self.directions:
            direction.draw(screen)
        self.draw(screen)
        self.update()
