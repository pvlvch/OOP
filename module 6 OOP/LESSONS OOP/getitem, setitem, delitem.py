class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Error index")

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError("Need int index")

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)
        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Need int index")
        del self.marks[key]


danil = Students('Danil', [2,2,2,3,4])
danil[10] = 5
del danil[0]
print(danil.marks)
