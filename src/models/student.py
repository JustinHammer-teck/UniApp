from __future__ import annotations
from typing import List
from .subject import Subject


class Student:
    id: str
    name: str
    email: str
    password: str
    enrolments: List[Subject]

    def __init__(self, id: str, name: str, email: str, password: str) -> None:
        self.id, self.name, self.email, self.password = id, name, email, password
        self.enrolments = []

    def __str__(self) -> str:
        return f"Id: {self.id} - Name {self.name} - Email {self.email} - Enrolments: {len(self.enrolments)}"

    @staticmethod
    def create_student(id: str, name: str, email: str, password: str) -> Student:
        return Student(id, name, email, password)

    def is_fully_enrol(self) -> bool:
        return self.__is_exceeded_enrolment()

    def enrol_subject(self, subject: Subject):
        if not self.__is_exceeded_enrolment():
            self.enrolment.append(subject)
        else:
            print("Student Exceeded Subject Enrolment Capacity")

    def delete_subject(self, subjectId: int):
        self.enrolments

    def __is_exceeded_enrolment(self) -> bool:
        return len(self.enrolments) => 4
