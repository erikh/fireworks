from cell import Cell


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

    def __init__(self, x, y, bearing, distance):
        self.x = x
        self.y = y
        self.bearing = bearing
        self.distance = distance

    def spread(self, distance=1):
        self.distance += distance

    def draw(self, screen):
        x = self.x
        y = self.y

        match self.bearing:
            case self.Up:
                for _ in range(self.distance):
                    y -= 1

                    if y >= 0:
                        screen.grid[y][x].set_orientation(Cell.OrientationTop)
            case self.UpLeft:
                for _ in range(self.distance):
                    y -= 1
                    x -= 1

                    if y >= 0 and x >= 0:
                        screen.grid[y][x].\
                                set_orientation(Cell.OrientationTopLeft)
            case self.UpRight:
                for _ in range(self.distance):
                    y -= 1
                    x += 1

                    if y >= 0 and x < len(screen.grid[y])-1:
                        screen.grid[y][x].\
                                set_orientation(Cell.OrientationTopRight)
            case self.Down:
                for _ in range(self.distance):
                    y += 1

                    if y < len(screen.grid)-1:
                        screen.grid[y][x]\
                                .set_orientation(Cell.OrientationBottom)
            case self.DownLeft:
                for _ in range(self.distance):
                    y += 1
                    x -= 1

                    if y < len(screen.grid)-1 and x >= 0:
                        screen.grid[y][x].\
                                set_orientation(Cell.OrientationBottomLeft)
            case self.DownRight:
                for _ in range(self.distance):
                    y += 1
                    x += 1

                    if y < len(screen.grid)-1 and x < len(screen.grid[y])-1:
                        screen.grid[y][x].\
                                set_orientation(Cell.OrientationBottomRight)
            case self.Left:
                for _ in range(self.distance):
                    x -= 1

                    if x >= 0:
                        screen.grid[y][x].set_orientation(Cell.OrientationLeft)
            case self.Right:
                for _ in range(self.distance):
                    x += 1

                    if x < len(screen.grid[y])-1:
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
            case self.UpLeft:
                for _ in range(self.distance):
                    y -= 1
                    x -= 1

                    if y >= 0 and x >= 0:
                        screen.grid[y][x].set_orientation(None)
            case self.UpRight:
                for _ in range(self.distance):
                    y -= 1
                    x += 1

                    if y >= 0 and x < len(screen.grid[y])-1:
                        screen.grid[y][x].set_orientation(None)
            case self.Down:
                for _ in range(self.distance):
                    y += 1

                    if y < len(screen.grid)-1:
                        screen.grid[y][x].set_orientation(None)
            case self.DownLeft:
                for _ in range(self.distance):
                    y += 1
                    x -= 1

                    if y < len(screen.grid)-1 and x >= 0:
                        screen.grid[y][x].set_orientation(None)
            case self.DownRight:
                for _ in range(self.distance):
                    y += 1
                    x += 1

                    if y < len(screen.grid)-1 and x < len(screen.grid[y])-1:
                        screen.grid[y][x].set_orientation(None)
            case self.Left:
                for _ in range(self.distance):
                    x -= 1

                    if x >= 0:
                        screen.grid[y][x].set_orientation(None)
            case self.Right:
                for _ in range(self.distance):
                    x += 1

                    if x < len(screen.grid[y])-1:
                        screen.grid[y][x].set_orientation(None)
