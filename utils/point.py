from utils.math import clamp


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __abs__(self):
        return Point(abs(self.x), abs(self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == self.y

    def increase_by_magnitude(self, mag):
        return Point(self.x * mag, self.y * mag)

    def direction(self):
        return Point(clamp(self.x, 1, -1), clamp(self.y, 1, -1))
