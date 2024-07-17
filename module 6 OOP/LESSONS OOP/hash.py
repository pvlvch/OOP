class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

c1 = Point(1,2)
c2 = Point(2,2)
print(c1 == c2)
print(hash(c1), hash(c2))