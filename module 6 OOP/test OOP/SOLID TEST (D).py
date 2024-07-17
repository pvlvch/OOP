from abc import ABC, abstractmethod
from typing import List
class Student:
    def __init__(self, name: str, id_student: int):
        self.name = name
        self.id_student = id_student

class IStudentRepository(ABC):
    @abstractmethod
    def add_students(self, student: Student) -> None:
        pass

    @abstractmethod
    def get_student(self) -> List[Student]:
        pass

class StudentRepository(IStudentRepository):
    def __init__(self):
        self.students = []

    def add_students(self, student: Student) -> None:
        self.students.append(student)

    def get_student(self) -> List[Student]:
        return self.students


class StudentService:
    def __init__(self, repository: IStudentRepository):
        self.repository = repository

    def register_students(self, name: str, id_student: int) -> None:
        student = Student(name, id_student)
        self.repository.add_students(student)


reposit = StudentRepository()
student_service = StudentService(reposit)
student_service.register_students(name="John Cena", id_student=1)
student_service.register_students(name="Kirill Vu", id_student=2)
student_service.register_students(name="Evgen Jackson", id_student=3)
students = reposit.get_student()
for student in students:
    print(f"{student.name} с номером студенческого {student.id_student}")