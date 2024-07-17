class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    def __str__(self):
        return f"{self.name}"


res = Cat("Dasha")
print(res)

class Numbers:
    def __init__(self, *args):
        self.__numb = args

    def __len__(self):
        return len(self.__numb)

    def __abs__(self):
        return list(map(abs, self.__numb))

p = Numbers(1,2,3,-4)
print(len(p))
print(abs(p))