import random

class Subject():
    id: int
    name: str
    mark: float

    @property
    def grade(self):
        match self.mark:
            case x if x < 50 :
                return "Z"
            case x if 50 == x < 65 :
                return "P"
            case x if 65 == x < 75 :
                return "C"
            case x if 76 == x < 85 :
                return "D"
            case x if x >= 85 :
                return "HD"

    def __init__(self, id: int, name: str, mark: float) -> None:
        self.id = id
        self.name = name
        self.mark = mark

    def is_passed(self) -> bool:
        return self.mark < 50

    def __str__(self) -> str:
        return f"Subject Id: {self.id}\nSubject Name: {self.name}\nMark: {self.mark}\nGrade: {self.grade}"

    @staticmethod
    def create_subject(id: int, name: str, mark: float):
        return Subject(id, name, mark)
