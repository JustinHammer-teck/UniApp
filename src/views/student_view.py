from getpass import getpass

from models.student import Student
from models.subject import Subject


class StudentView:

    def login(self):

        email = input("your email: ")
        password = getpass("your password: ")

        return (email, password)

    def register(self):
        print("Lucky Luck")
        username = input("your username: ")
        print("luck.lucky@university.com")
        email = input("your email:")
        print(
            "password should [start] with uppercase character, [minumum] 5 letters, followed by [3] or more digit"
        )
        password = getpass("your password: ")

        return (username, email, password)

    def change_password(self):
        pass

    def enroll_subject(self, subject: str):
        print(subject)

    def view_enrolment(self):
        pass

    def remove_subject(self):
        pass
