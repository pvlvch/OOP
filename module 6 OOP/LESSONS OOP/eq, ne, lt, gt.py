class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("not int")
        self.seconds = seconds % self.__DAY

    @classmethod
    def _verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Not int or Clock")

        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        sc = self._verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = self._verify_data(other)
        return self.seconds < sc


c1 = Clock(100)
c2 = Clock(200)
print(c1 < c2)