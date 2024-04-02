from getpass import getpass
from typing import List
from models.student import Student


class StudentView:

    def login(self):

        username = input("your username: ")
        password = getpass("your password: ")

        return (username, password)

    def view_enrolment(self, enrolment: List[Student]):
        pass
