import random
import re
from typing import List

from common.color import Color
from persistent import db
from models.student import Student
from models.subject import Subject
from views import student_view as studentv


class StudentController:
    EMAIL_PATTERN = r"^[a-zA-Z]+\.+[a-zA-Z]+@university\.com$"
    PASSWORD_PATTERN = r"^[A-Z][A-Za-z]{6,}\d{3,}$"

    def __init__(self) -> None:
        self.view, self.db = (
            studentv.StudentView(),
            db.Database(),
        )

    def login(self) -> Student | None:
        Color.prGreen("\tStudent Sign In")

        while True:
            (email, password) = self.view.login()

            if self.__validate_email(email) and self.__validate_password(password):
                Color.prYellow(f"\temail and password formats acceptable")
                selected_student = self.__is_registed_user(email, password)

                if selected_student:
                    return selected_student[0]
                else:
                    Color.prRed("\tStudent does not exist")
                    break
            else:
                Color.prRed("\tIncorrect email or password format")

    def register(self):
        Color.prGreen("\tStudent Sign Up")
        while True:
            (email, password) = self.view.register_step1()

            if self.__validate_email(email) and self.__validate_password(password):
                Color.prYellow(f"\tEmail and password formats acceptable")
                if self.__is_existed_user(email):
                    existing_student = self.__get_existing_student(email)
                    Color.prRed(f"\tStudent {existing_student.name} already exists")
                    break
                else:
                    username = self.view.register_step2()
                    if username:  # Additional check to ensure `username` is not empty
                        new_student: Student = Student.create_student(
                            username, email, password
                        )
                        self.db.context.append(new_student)
                        self.db.save()
                        Color.prYellow(f"\tEnrolling Student {new_student.name}")
                        break
            else:
                Color.prRed("\tIncorrect email or password format")

    def __get_existing_student(self, email: str) -> Student | None:
        existing_students = [
            student
            for student in self.db.read()
            if student.email.lower() == email.lower()
        ]
        existing_students = [
            student
            for student in self.db.read()
            if student.email.lower() == email.lower()
        ]
        if existing_students:
            return existing_students[0]
        return None

    def change_password(self, ctx: Student):
        students = [st for st in self.db.read() if st.id == ctx.id]

        if not students:
            raise Exception(f"\t\tCould not find student with id {ctx.id}")

        student = students[0]

        (newpassword, confirmnewpassword) = self.view.get_new_password()

        if self.__validate_password(newpassword):
            student.update_password(newpassword)
            self.db.save()
            return
        else:
            Color.prRed("\t\tIncorrect password format")
            return

    def enrol_subject(self, ctx: Student):
        new_id = str(random.randint(1, 999)).zfill(3)
        new_subject: Subject = Subject.create_subject(
            new_id, f"Subject-{new_id}", random.randint(45, 100)
        )
        students = [st for st in self.db.read() if st.id == ctx.id]

        if not students:
            raise Exception(f"\t\tCould not find student with id {ctx.id}")

        entity: Student = students[0]

        if not entity.enrol_subject(new_subject):
            return

        self.db.save()
        self.view.enrol_subject(entity, new_subject)

    def view_enrolment(self, ctx: Student):
        students = [st for st in self.db.read() if st.id == ctx.id]

        if not students:
            raise Exception(f"\t\tCould not find student with id {ctx.id}")

        self.view.view_enrolment(students[0])

    def remove_subject(self, ctx: Student):
        students = [st for st in self.db.read() if st.id == ctx.id]

        if not students:
            raise Exception(f"\t\tCould not find student with id {ctx.id}")

        student = students[0]

        remove_subject_id = self.view.remove_subject()

        subject_found = False
        for subject in student.enrolment:
            if subject.id == remove_subject_id:
                subject_found = True
                student.delete_subject(remove_subject_id)
                Color.prYellow(f"\t\tDropping Subject-{remove_subject_id}")
                Color.prYellow(
                    f"\t\tYou are now enrolled in {len(student.enrolment)} out of 4 subjects "
                )
                break

        if not subject_found:
            Color.prRed(f"\t\tSubject-{remove_subject_id} not found - Try Again")
            return

        self.db.save()

    def __validate_password(self, password: str):
        return re.match(self.PASSWORD_PATTERN, password)

    def __validate_email(self, email: str):
        return re.match(self.EMAIL_PATTERN, email)

    def __is_existed_user(self, email: str) -> bool:
        return (
            len(
                [
                    student
                    for student in self.db.read()
                    if student.email.lower() == email.lower()
                ]
            )
            > 0
        )

    def __is_registed_user(self, email: str, password: str) -> List[Student]:
        return [
            student
            for student in self.db.read()
            if student.email.lower() == email.lower()
            and student.password.lower() == password.lower()
        ]
