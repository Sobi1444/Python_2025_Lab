class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, x, y, width, height):
        # x i y to lewy dolny rog
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @classmethod
    def from_points(cls, points):
        # tworzy prostokat z listy lub krotki dwoch punktow
        p1, p2 = points
        x = min(p1.x, p2.x)
        y = min(p1.y, p2.y)
        width = abs(p2.x - p1.x)
        height = abs(p2.y - p1.y)
        return cls(x, y, width, height)

    @property
    def left(self):
        return self.x

    @property
    def bottom(self):
        return self.y

    @property
    def right(self):
        return self.x + self.width

    @property
    def top(self):
        return self.y + self.height

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)

    @property
    def center(self):
        return Point(self.x + self.width / 2, self.y + self.height / 2)