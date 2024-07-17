class Course:
    "O"
    def __init__(self, title: str):
        self._title = title


class LectionCourses(Course):
    def __init__(self, title: str, lection: str):
        super().__init__(title)
        self._lection = lection


class LabCourses(Course):
    def __init__(self, title: str, labs: str):
        super().__init__(title)
        self._labs = labs


lect = LectionCourses("Lecture on OOP", "SOLID")
lab = LabCourses("Labs on OOP", "O-C")



class Sports:
    def __init__(self, sport: str):
        self.sport = sport


class Football(Sports):
    def __init__(self, sport, players: int):
        super().__init__(sport)
        self.players = players


class Hockey(Sports):
    def __init__(self, sport, players: int):
        super().__init__(sport)
        self.players = players


foot = Football("football", 11)
hock = Hockey("Hockey", 9)