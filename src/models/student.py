from .subject import Subject


class Student:
    id: str
    name: str
    email: str
    password: str
    subjects: list[Subject]

    def __init__(self, id: str, name: str, email: str, password: str):
        self.id, self.name, self.email, self.password = id, name, email, password

    @staticmethod
    def create_student(id: str, name: str, email: str, password: str):
        return Student(id, name, email, password)

    def add_subject(self, subject: Subject):
        self.subjects.append(subject)

    def delete_subject(self, subjectId: int):
        self.subjects
