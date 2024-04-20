from getpass import getpass

from common.color import Color
from models.student import Student
from models.subject import Subject


class StudentView:

    def login(self):
        Color.prGreen("Student Sign In")

        email = input("your email: ")
        password = getpass("your password: ")

        return (email, password)

    def register_step1(self):
        Color.prGreen("Student Sign Up")

        print("eg: luck.lucky@university.com")
        email = input("your email:")
        print(
            "password should [start] with uppercase character, [minumum] 5 letters, followed by [3] or more digit"
        )
        password = getpass("your password: ")
        confirmpassword = getpass("confirm your password: ")

        return (email, password, confirmpassword)

    def register_step2(self):
        print("eg: Lucky Luck")
        username = input("your username: ")

        return username

    def get_new_password(self):
        Color.prYellow("Updating Password")

        newpassword = getpass("New Password: ")
        confirmnewpassword = getpass("Confirm Parrsowrd: ")

        return (newpassword, confirmnewpassword)

    def enrol_subject(self, subject: Subject):
        print(f"Enrolling in {subject.name}")

    def view_enrolment(self, student: Student):
        print(f"Showing {len(student.enrolment)}")
        if student.enrolment:
            for subject in student.enrolment:
                print(subject.__str__())

    def remove_subject(self):
        pass
