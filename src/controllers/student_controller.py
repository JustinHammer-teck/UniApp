import re
from ..models import student, db
from ..views import student_view as studentv


class StudentController:

    def __init__(self) -> None:
        self.view, self.model, self.db = (
            studentv.StudentView(),
            student.Student,
            db.Database(),
        )

    def login(self):
        (username, password) = self.view.login()

        email_pattern = r"^[a-zA-Z]+\.+[a-zA-Z]+@university\.com$"
        password_pattern = r"^[A-Z][A-Za-z]{4,}\d{3,}$"

        if re.match(email_pattern, username) and re.match(password_pattern, password):
            return (True, "")
        else:
            # print("Invalid Username or Password, please try again")
            return (False, "Invalid Username or Password, please try again")

    def register(self):
        (username, password) = self.view.login()

        email_pattern = r"^[a-zA-Z]+\.+[a-zA-Z]+@university\.com$"
        password_pattern = r"^[A-Z][A-Za-z]{4,}\d{3,}$"

        if re.match(email_pattern, username) and re.match(password_pattern, password):
            ## TODO: add new user to db
            return (True, "")
        else:
            # print("Invalid Username or Password, please try again")
            return (False, "Invalid Username or Password, please try again")

    def enrol_subject(self):
        pass
