class Counter:
    def __init__(self, count):
        self.__count = count

    def __call__(self, step, *args, **kwargs):
        self.__count += step
        return self.__count

res = Counter(1)
res(1)
res(2)
print(res(3))
print(res.__dict__)