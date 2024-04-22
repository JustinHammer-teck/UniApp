class Subject:

    @property
    def grade(self):
        if self.mark < 50:
            return "Z"
        elif 50 <= self.mark < 65:
            return "P"
        elif 65 <= self.mark < 75:
            return "C"
        elif 75 <= self.mark < 85:
            return "D"
        elif self.mark >= 85:
            return "HD"

    def __init__(self, id: int, name: str, mark: float) -> None:
        self.id = id
        self.name = name
        self.mark = mark

    def is_passed(self) -> bool:
        return self.mark >= 50

    def __str__(self) -> str:
        return f"Subject Id:: {self.id} -- Mark: {self.mark} -- Grade: {self.grade}"

    @staticmethod
    def create_subject(id: int, name: str, mark: float):
        return Subject(id, name, mark)
