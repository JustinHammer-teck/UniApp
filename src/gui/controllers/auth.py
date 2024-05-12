from os.path import isjunction
import re

import tkinter.messagebox as tkmb
from typing import List

from gui.cores.controller import Controller
from gui.cores.core import Core
from models.student import Student
from persistent.db import Database


class AuthController(Controller):
    EMAIL_PATTERN = r"^[a-zA-Z]+\.+[a-zA-Z]+@university\.com$"
    PASSWORD_PATTERN = r"^[A-Z][A-Za-z]{6,}\d{3,}$"

    def __init__(self, core: Core) -> None:
        super().__init__()
        self.core = core
        self.db = Database()

    def login(self, username: str, password: str):
        if not (username and password):
            tkmb.showerror(
                title="Invalid Format",
                message="Email and password cannot be empty",
                icon="warning",
            )
            return

        if not (self.__validate_email(username) and self.__validate_password(password)):
            tkmb.showerror(
                title="Invalid Format",
                message="Incorrect email or password format",
                icon="warning",
            )
            return

        selected_student = self.__is_registed_user(username, password)

        if not selected_student:
            tkmb.showinfo(
                title="Not Found",
                message=f"User with {username} does not existed",
                icon="warning",
            )
            return

        self.core.is_auth = True
        self.core.user = selected_student[0]
        return self.core.controller("home")

    def logout(self):
        self.core.logout()
        return self.core.controller("auth")

    def main(self):
        self.view

    def __validate_password(self, password: str):
        return re.match(self.PASSWORD_PATTERN, password)

    def __validate_email(self, email: str):
        return re.match(self.EMAIL_PATTERN, email)

    def __is_registed_user(self, email: str, password: str) -> List[Student]:
        return [
            student
            for student in self.db.read()
            if student.email.lower() == email.lower()
            and student.password.lower() == password.lower()
        ]
