from random import choice


class Direction:
    Up = (0, -1)
    Down = (0, 1)
    Left = (-1, 0)
    Right = (1, 0)
    UpLeft = (-1, -1)
    UpRight = (1, -1)
    DownLeft = (-1, 1)
    DownRight = (1, 1)

    x = 0
    y = 0
    bearing = Up
    distance = 0
    eraseto = 0
    flare = False
    color = "white"

    def __init__(self, x, y, bearing, distance, flare, colors):
        self.x = x
        self.y = y
        self.bearing = bearing
        self.distance = distance
        self.eraseto = 0
        self.flare = flare
        self.colors = colors

    def spread(self, distance=1):
        self.distance += distance
        self.eraseto += distance

    def clear(self, screen):
        x = self.x
        y = self.y

        for _ in range(self.distance):
            x += self.bearing[0]
            y += self.bearing[1]

            if x >= 0 and y >= 0 and \
               y < len(screen.grid) and x < len(screen.grid[y]):
                screen.grid[y][x].set_empty()

    def draw(self, screen):
        x = self.x
        y = self.y

        for _ in range(self.distance):
            x += self.bearing[0]
            y += self.bearing[1]
            if x >= 0 and y >= 0 and \
               y < len(screen.grid) and x < len(screen.grid[y]):
                if self.flare:
                    screen.grid[y][x].set_fg(choice(self.colors))
                    screen.grid[y][x].set_explosion()
                elif self.bearing == self.Up:
                    screen.grid[y][x].set_fg(choice(self.colors))
                    screen.grid[y][x].set_rising()
        self.erase(screen)

    def erase(self, screen):
        x = self.x
        y = self.y

        for _ in range(self.eraseto):
            x += self.bearing[0]
            y += self.bearing[1]
            if x >= 0 and y >= 0 and \
               y < len(screen.grid) and x < len(screen.grid[y]):
                screen.grid[y][x].set_empty()
