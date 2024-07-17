class ThreadData:
    __shared_attrs = {
        "name": "Thread_1",
        "data": {},
        "id": 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


x = ThreadData()
x2 = ThreadData()
x2.id = 4
print(x.__dict__)