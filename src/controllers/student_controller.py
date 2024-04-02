import re
from ..models.student import Student
from ..views.student_view import StudentView


class StudentController:

    def __init__(self) -> None:
        self.view, self.model = StudentView(), Student

    def login(self) -> bool:
        (username, password) = self.view.login()

        email_pattern = r"^[a-zA-Z]+\.+[a-zA-Z]+@university\.com$"
        password_pattern = r"^[A-Z][A-Za-z]{4,}\d{3,}$"

        if re.match(email_pattern, username) and re.match(password_pattern, password):
            return True
        else:
            print("Invalid Username or Password, please try again")
            return False
