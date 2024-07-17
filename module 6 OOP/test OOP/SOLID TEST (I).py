from abc import ABC, abstractmethod


class ICourse(ABC):
    @abstractmethod
    def get_course_title(self) -> str:
        pass


class IExaminable(ABC):
    @abstractmethod
    def conduct_exam(self) -> None:
        pass


class LectureCourses(ICourse, IExaminable):
    def __init__(self, title: str, lecturer: str):
        self._title = title
        self._lecturer = lecturer

    def get_course_title(self) -> str:
        return self._title

    def conduct_exam(self) -> None:
        print(f"Conducting exam for lecture course: {self._title}")


class LabCourses(ICourse):
    def __init__(self, title: str, lab_instructor):
        self._title = title
        self._lab_instructor = lab_instructor

    def get_course_title(self) -> str:
        return self._title


lect = LectureCourses("Russian language", "Arseniy Popovich")
print(lect.get_course_title())
lect.conduct_exam()

labs = LabCourses("English language", "John Newston")
print(labs.get_course_title())