class Clock:
    __DAY = 86400


    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY


    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24

        return f"{self.__get_formated(h)}:{self.__get_formated(m)}:{self.__get_formated(s)}"


    @classmethod
    def __get_formated(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть целым числом")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds + sc)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        print("__iadd__")
        if isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть целым числом or Clock")

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds += other
        return self


c1 = Clock(1000)
c2 = 100 + c1
print(c1.get_time())


class Test:
    def __init__(self, year: int):
        if not isinstance(year, int):
            raise TypeError("Not int")
        self.year = year

    def get_year(self):
        return self.year

    def __mul__(self, other):
        if not isinstance(other, (int, Test)):
            raise ArithmeticError("int or clock")
        ye = other
        if isinstance(other, Test):
            ye = other.year
        return Test(self.year * ye)

    def __imul__(self, other):
        if not isinstance(other, (int, Test)):
            raise ArithmeticError("int or clock")

        ye = other
        if isinstance(other, Test):
            ye = other.year
        self.year *= ye
        return self



age1 = Test(100)
age1 *= 2000
print(age1.get_year())