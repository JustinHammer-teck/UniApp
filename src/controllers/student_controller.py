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
    PASSWORD_PATTERN = r"^[A-Z][A-Za-z]{4,}\d{3,}$"

    def __init__(self) -> None:
        self.view, self.db = (
            studentv.StudentView(),
            db.Database(),
        )

    def login(self) -> Student | None:

        result: Student | None = None

        while type(result) is not Student:
            (email, password) = self.view.login()

            selected_student = self.__is_registed_user(email, password)

            if not selected_student:
                Color.prRed(f"Wrong Email or Password, please try again")
                return

            return selected_student[0]

    def register(self):

        result = False

        while not result:
            (email, password, confirmpassword) = self.view.register_step1()

            if not password == confirmpassword:
                Color.prRed("Your confim password is not identical with your password")
                return
            if self.__is_existed_user(email):
                Color.prRed("User already exist, please try again")
                return
            elif self.__validate_email(email) and self.__validate_password(password):
                username = self.view.register_step2()

                new_student: Student = Student.create_student(username, email, password)

                self.db.context.append(new_student)

                self.db.save()

                result = True

                Color.prGreen(f"Successfully Create User: {new_student.name}")

                break
            else:
                Color.prRed("Invalid Email or Password format, please try again")
                return

    def change_password(self, ctx: Student):
        pass

    def enrol_subject(self, ctx: Student):
        new_id = random.randint(1, 1000)
        new_subject: Subject = Subject.create_subject(
            new_id, f"Subject {new_id}", random.randint(45, 100)
        )
        students = [st for st in self.db.read() if st.id == ctx.id]

        if not students:
            raise Exception(f"Could not find student with id {ctx.id}")

        entity: Student = students[0]

        if entity.enrol_subject(new_subject):
            return

        self.db.save()
        self.view.enrol_subject(new_subject)

    def view_enrolment(self, ctx: Student):
        students = [st for st in self.db.read() if st.id == ctx.id]

        if not students:
            raise Exception(f"Could not find student with id {ctx.id}")

        self.view.view_enrolment(students[0])

    def get_subject_info(self, ctx: Student):
        pass

    def remove_subject(self, ctx: Student):
        pass

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
