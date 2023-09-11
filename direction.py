class Direction:
    Up = 0
    Down = 1
    Left = 2
    Right = 3
    UpLeft = 4
    UpRight = 5
    DownLeft = 6
    DownRight = 7

    x = 0
    y = 0
    bearing = Up
    distance = 0
    eraseto = 0
    flare = False
    color = "white"

    def __init__(self, x, y, bearing, distance, flare, color):
        self.x = x
        self.y = y
        self.bearing = bearing
        self.distance = distance
        self.eraseto = 0
        self.flare = flare
        self.color = color

    def spread(self, distance=1):
        self.distance += distance
        self.eraseto += distance

    def clear(self, screen):
        x = self.x
        y = self.y

        match self.bearing:
            case self.Up:
                for _ in range(self.distance):
                    y -= 1

                    if y >= 0:
                        screen.grid[y][x].set_empty()
            case self.UpLeft:
                for d in range(self.distance):
                    y -= 1
                    x -= 1

                    if y >= 0 and x >= 0:
                        screen.grid[y][x].set_empty()

            case self.UpRight:
                for _ in range(self.distance):
                    y -= 1
                    x += 1

                    if y >= 0 and x < len(screen.grid[y])-1:
                        screen.grid[y][x].set_empty()

            case self.Down:
                for _ in range(self.distance):
                    y += 1

                    if y < len(screen.grid)-1:
                        screen.grid[y][x].set_empty()
            case self.DownLeft:
                for _ in range(self.distance):
                    y += 1
                    x -= 1

                    if y < len(screen.grid)-1 and x >= 0:
                        screen.grid[y][x].set_empty()
            case self.DownRight:
                for _ in range(self.distance):
                    y += 1
                    x += 1

                    if y < len(screen.grid)-1 and x < len(screen.grid[y])-1:
                        screen.grid[y][x].set_empty()
            case self.Left:
                for _ in range(self.distance):
                    x -= 1

                    if x >= 0:
                        screen.grid[y][x].set_empty()
            case self.Right:
                for _ in range(self.distance):
                    x += 1

                    if x < len(screen.grid[y])-1:
                        screen.grid[y][x].set_empty()

    def draw(self, screen):
        x = self.x
        y = self.y

        match self.bearing:
            case self.Up:
                for _ in range(self.distance):
                    y -= 1

                    if y >= 0:
                        screen.grid[y][x].set_fg(self.color)
                        if self.flare:
                            screen.grid[y][x].set_explosion()
                        else:
                            screen.grid[y][x].set_rising()
            case self.UpLeft:
                for d in range(self.distance):
                    y -= 1
                    x -= 1

                    if y >= 0 and x >= 0:
                        if self.flare:
                            screen.grid[y][x].set_fg(self.color)
                            screen.grid[y][x].set_explosion()

            case self.UpRight:
                for _ in range(self.distance):
                    y -= 1
                    x += 1

                    if y >= 0 and x < len(screen.grid[y])-1:
                        if self.flare:
                            screen.grid[y][x].set_fg(self.color)
                            screen.grid[y][x].set_explosion()

            case self.Down:
                for _ in range(self.distance):
                    y += 1

                    if y < len(screen.grid)-1:
                        if self.flare:
                            screen.grid[y][x].set_fg(self.color)
                            screen.grid[y][x].set_explosion()
            case self.DownLeft:
                for _ in range(self.distance):
                    y += 1
                    x -= 1

                    if y < len(screen.grid)-1 and x >= 0:
                        if self.flare:
                            screen.grid[y][x].set_fg(self.color)
                            screen.grid[y][x].set_explosion()
            case self.DownRight:
                for _ in range(self.distance):
                    y += 1
                    x += 1

                    if y < len(screen.grid)-1 and x < len(screen.grid[y])-1:
                        if self.flare:
                            screen.grid[y][x].set_fg(self.color)
                            screen.grid[y][x].set_explosion()
            case self.Left:
                for _ in range(self.distance):
                    x -= 1

                    if x >= 0:
                        if self.flare:
                            screen.grid[y][x].set_fg(self.color)
                            screen.grid[y][x].set_explosion()
            case self.Right:
                for _ in range(self.distance):
                    x += 1

                    if x < len(screen.grid[y])-1:
                        if self.flare:
                            screen.grid[y][x].set_fg(self.color)
                            screen.grid[y][x].set_explosion()
        self.erase(screen)

    def erase(self, screen):
        x = self.x
        y = self.y

        match self.bearing:
            case self.Up:
                for _ in range(self.eraseto):
                    y -= 1

                    if y >= 0:
                        screen.grid[y][x].set_empty()
            case self.UpLeft:
                for _ in range(self.eraseto):
                    y -= 1
                    x -= 1

                    if y >= 0 and x >= 0:
                        screen.grid[y][x].set_empty()
            case self.UpRight:
                for _ in range(self.eraseto):
                    y -= 1
                    x += 1

                    if y >= 0 and x < len(screen.grid[y])-1:
                        screen.grid[y][x].set_empty()
            case self.Down:
                for _ in range(self.eraseto):
                    y += 1

                    if y < len(screen.grid)-1:
                        screen.grid[y][x].set_empty()
            case self.DownLeft:
                for _ in range(self.eraseto):
                    y += 1
                    x -= 1

                    if y < len(screen.grid)-1 and x >= 0:
                        screen.grid[y][x].set_empty()
            case self.DownRight:
                for _ in range(self.eraseto):
                    y += 1
                    x += 1

                    if y < len(screen.grid)-1 and x < len(screen.grid[y])-1:
                        screen.grid[y][x].set_empty()
            case self.Left:
                for _ in range(self.eraseto):
                    x -= 1

                    if x >= 0:
                        screen.grid[y][x].set_empty()
            case self.Right:
                for _ in range(self.eraseto):
                    x += 1

                    if x < len(screen.grid[y])-1:
                        screen.grid[y][x].set_empty()
