from utils.math import clamp


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __abs__(self):
        return Point(abs(self.x), abs(self.y))

    def __len__(self):
        temp = abs(self)
        return temp.x + temp.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x},{self.y})"

    def reduce_to_one(self):
        return Point(clamp(self.x, -1, 1), clamp(self.y, -1, 1))

    def move_towards(self, other):
        distance = other - self
        if abs(distance).x > 1 or abs(distance).y > 1:
            return self + distance.reduce_to_one()
        return self
