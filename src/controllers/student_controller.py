import re
from typing import List, Tuple
from ..models import student, db
from ..views import student_view as studentv


class StudentController:

    def __init__(self) -> None:
        self.view, self.model, self.db = (
            studentv.StudentView(),
            student.Student,
            db.Database(),
        )

    def login(self) -> Tuple[student.Student | None, str]:
        (username, password) = self.view.login()

        email_pattern = r"^[a-zA-Z]+\.+[a-zA-Z]+@university\.com$"
        password_pattern = r"^[A-Z][A-Za-z]{4,}\d{3,}$"

        if re.match(email_pattern, username) and re.match(password_pattern, password):
            students: List[student.Student] = self.__is_registed_user(
                username, password
            )

            if students:
                return (students[0], "")
            else:
                return (None, "Invalid Username or Password, please try again")
        else:
            return (None, "Invalid Username or Password, please try again")

    def register(self):
        (username, password) = self.view.register()

        email_pattern = r"^[a-zA-Z]+\.+[a-zA-Z]+@university\.com$"
        password_pattern = r"^[A-Z][A-Za-z]{4,}\d{3,}$"

        if self.__is_exited_user(username):
            return (False, "user already exist")
        elif re.match(email_pattern, username) and re.match(password_pattern, password):
            return (True, "")
        else:
            return (False, "Invalid Username or Password, please try again")

    def __is_exited_user(self, username: str) -> bool:
        students: List[student.Student] = self.db.read()

        return [
            student for student in students if student.email.lower() == username.lower()
        ][0] is not None

    def __is_registed_user(self, username: str, password: str) -> List[student.Student]:
        students: List[student.Student] = self.db.read()

        return [
            student
            for student in students
            if student.email.lower() == username.lower()
            and student.password.lower() == password.lower()
        ]
