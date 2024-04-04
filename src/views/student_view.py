from getpass import getpass

from ..models.student import Student
from ..models.subject import Subject


class StudentView:

    def login(self):

        username = input("your username: ")
        password = getpass("your password: ")

        return (username, password)

    def register(self):
        username = input("your email: ")
        password = getpass("your password: ")

        return (username, password)

    def change_password(self):
        pass

    def enrol_subject(self, subject: Subject):
        pass

    def view_enrolment(self):
        pass

    def remove_subject(self, student: Student):
        pass
