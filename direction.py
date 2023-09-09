from cell import Cell


class Direction:
    Up = 0
    Down = 1
    Left = 2
    Right = 3

    x = 0
    y = 0
    bearing = Up
    distance = 0

    def __init__(self, x, y, bearing, distance):
        self.x = x
        self.y = y
        self.bearing = bearing
        self.distance = distance

    def spread(self):
        self.distance += 1

    def draw(self, screen):
        x = self.x
        y = self.y

        match self.bearing:
            case self.Up:
                for _ in range(self.distance):
                    y -= 1

                    if y >= 0:
                        screen.grid[y][x].set_orientation(Cell.OrientationTop)
            case self.Down:
                for _ in range(self.distance):
                    y += 1

                    if y < screen.grid.len():
                        screen.grid[y][x]\
                                .set_orientation(Cell.OrientationBottom)
            case self.Left:
                for _ in range(self.distance):
                    x -= 1

                    if x >= 0:
                        screen.grid[y][x].set_orientation(Cell.OrientationLeft)
            case self.Right:
                for _ in range(self.distance):
                    x += 1

                    if x < screen.grid[y].len():
                        screen.grid[y][x].set_orientation(Cell.OrientationLeft)

    def erase(self, screen):
        x = self.x
        y = self.y

        match self.bearing:
            case self.Up:
                for _ in range(self.distance):
                    y -= 1

                    if y >= 0:
                        screen.grid[y][x].set_orientation(None)
            case self.Down:
                for _ in range(self.distance):
                    y += 1

                    if y < screen.grid.len():
                        screen.grid[y][x].set_orientation(None)
            case self.Left:
                for _ in range(self.distance):
                    x -= 1

                    if x >= 0:
                        screen.grid[y][x].set_orientation(None)
            case self.Right:
                for _ in range(self.distance):
                    x += 1

                    if x < screen.grid[y].len():
                        screen.grid[y][x].set_orientation(None)
