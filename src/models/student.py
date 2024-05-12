from __future__ import annotations

import random
from typing import List

from common.color import Color
from models.subject import Subject


class Student:
    id: str
    name: str
    email: str
    password: str
    enrolment: List[Subject]

    def __init__(self, name: str, email: str, password: str) -> None:
        self.id = str(random.randint(1, 999999)).zfill(6)
        self.name, self.email, self.password = name, email, password
        self.enrolment = []

    def __str__(self) -> str:
        return f"{self.name} :: {self.id} --> Email: {self.email}"

    @staticmethod
    def create_student(name: str, email: str, password: str) -> Student:
        return Student(name, email, password)

    def is_fully_enrol(self) -> bool:
        return self.__is_exceeded_enrolment()

    def enrol_subject(self, subject: Subject):
        if not self.__is_exceeded_enrolment():
            self.enrolment.append(subject)
            return True

        Color.prRed("\t\tStudents are allowed to enrol in 4 subjects only")
        return False

    def delete_subject(self, subject_id: str):
        for subject in self.enrolment:
            if subject.id == subject_id:
                self.enrolment.remove(subject)
                return

    def __is_exceeded_enrolment(self) -> bool:
        return len(self.enrolment) >= 4

    def update_password(self, new_password: str):
        self.password = new_password
        return self.password

    def average_score(self) -> float:
        if len(self.enrolment) == 0:
            return -1
        return sum(subject.mark for subject in self.enrolment) / len(self.enrolment)
