class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return self.x * self.x + self.y + self.y

    def __bool__(self):
        return self.x == self.y

    @classmethod
    def test_if(cls):
        if p1:
            print(True)
        else:
            print(False)

p1 = Point(2,3)
p1.test_if()