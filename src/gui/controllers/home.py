import random
import tkinter.messagebox as tkmb
from typing import List
from gui.cores.controller import Controller
from models.student import Student
from models.subject import Subject
from persistent.db import Database


class HomeController(Controller):
    def __init__(self, core) -> None:
        super().__init__()
        self.core = core
        self.db = Database()

    def get_subjects(self, student_id: int) -> List[Subject]:
        entity = self.get_student_with_id(student_id)
        return entity.enrolment

    def enrol_subject(self, student_id: int):
        entity = self.get_student_with_id(student_id)

        new_id = str(random.randint(1, 999)).zfill(3)
        new_subject: Subject = Subject.create_subject(
            new_id, f"Subject-{new_id}", random.randint(45, 100)
        )

        if not entity.enrol_subject(new_subject):
            tkmb.showerror(
                title="Enrolment Error",
                message="Student is allow to enrol 4 subject only",
                icon=tkmb.WARNING,
            )

        self.db.save()
        return self.core.controller("home")

    def get_student_with_id(self, student_id: int) -> Student:
        entities = [student for student in self.db.read() if student.id == student_id]
        return entities[0]

    def main(self):
        self.view
