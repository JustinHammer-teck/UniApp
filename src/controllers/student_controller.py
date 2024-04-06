import random
import re
from typing import List, Tuple

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

    def login(self) -> Tuple[Student | None, str]:
        (email, password) = self.view.login()

        if not self.__is_valid_login_session(email, password):
            return (None, "Invalid Username or Password, please try again")

        selected_student = [
            student
            for student in self.db.context
            if student.email.lower() == email.lower()
            and student.password.lower() == password.lower()
        ]

        if not selected_student:
            return (None, "Invalid Username or Password, please try again")

        return (selected_student[0], "Login Successfully")

    def register(self):
        (username, email, password) = self.view.register()

        if self.__is_exited_user(username):
            return "User already exist, please try again"
        elif self.__validate_email(email) and self.__validate_password(password):
            new_student: Student = Student.create_student(username, email, password)

            self.db.context.append(new_student)

            self.db.save()

            return "Successfully Create User"
        else:
            return "Invalid Username or Password, please try again"

    def change_password(self, ctx: Student):
        pass

    def enrol_subject(self, ctx: Student):

        new_subject: Subject = Subject.create_subject(
            1, "Subject 1", random.randint(45, 100)
        )
        students = [st for st in self.db.context if st.id == ctx.id]

        if not students:
            raise Exception(f"Could not find student with id {ctx.id}"f"Could not find student with id {ctx.id}")

        entity: Student = students[0]
        entity.enrol_subject(new_subject)

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

    def __is_valid_login_session(self, email, password):
        return (
            self.__validate_email(email)
            and self.__validate_password(password)
            and self.__is_registed_user(email, password)
        )

    def __validate_password(self, password: str):
        return re.match(self.PASSWORD_PATTERN, password)

    def __validate_email(self, email: str):
        return re.match(self.EMAIL_PATTERN, email)

    def __is_exited_user(self, username: str) -> bool:
        students: List[Student] = self.db.read()

        return [
            student for student in students if student.email.lower() == username.lower()
        ][0] is not None

    def __is_registed_user(self, username: str, password: str) -> List[Student]:
        students: List[Student] = self.db.read()

        return [
            student
            for student in students
            if student.email.lower() == username.lower()
            and student.password.lower() == password.lower()
        ]
