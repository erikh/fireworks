class Color:
    red = 255
    green = 255
    blue = 255

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return "#%x%x%x" % (self.red, self.green, self.blue)
