class Student:
    "S"
    def __init__(self, name: str, student_id: int):
        self._name = name
        self._student_id = student_id


class Grade:
    def __init__(self, student: Student, courses: str, grades: list):
        self._student = student
        self._courses = courses
        self._grades = list(grades)


kirill = Student("Kirill", 503606)
grades_kirill = Grade(kirill, "IT", [70,70,65,97,100,82])
print(kirill.__dict__)
print(grades_kirill.__dict__)

class Shop:
    def __init__(self, name_shop: str, address: str):
        self.name_shop = name_shop
        self.address = address

class Products:
    def __init__(self, shop: Shop, product):
        self.shop = shop
        self.product = list(product)