class Person:
    "L"
    def __init__(self, name: str):
        self._name = name


class Student(Person):
    def __init__(self, name: str, student_id: int):
        super().__init__(name)
        self._student_id = student_id


class Professor(Person):
    def __init__(self, name: str, department: str):
        super().__init__(name)
        self._department = department


kirill = Person("Kirill")
danil = Student("Danil", 10001)
vova = Professor("Vova", "IT")
print(kirill.__dict__, danil.__dict__, vova.__dict__)