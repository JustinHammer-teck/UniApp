from getpass import getpass

from common.color import Color
from models.student import Student
from models.subject import Subject


class StudentView:

    def login(self):
        email = input("Email: ")
        password = input("Password: ")

        return (email, password)

    def register_step1(self):
        email = input("Email: ")
        password = input("Password: ")

        return (email, password)

    def register_step2(self):
        while True:
            username = input("Name: ").strip()
            if username:  # Ensure the input is not empty or just whitespace
                return username
            else:
                print("Name cannot be empty. Please enter a valid name.")

    def get_confirm_password(self, newpassword):
        confirmnewpassword = input("Confirm Password: ")
        while confirmnewpassword != newpassword:
            Color.prRed("Password does not match - try again")
            return self.get_confirm_password(newpassword)

        return confirmnewpassword

    def get_new_password(self):
        Color.prYellow("Updating Password")
        newpassword = input("New Password: ")
        confirmnewpassword = self.get_confirm_password(newpassword)

        return (newpassword, confirmnewpassword)

    def enrol_subject(self, student: Student, subject: Subject):
        Color.prYellow(f"Enrolling in {subject.name}")
        Color.prYellow(
            f"You are now enrolled in {len(student.enrolment)} out of 4 subjects"
        )

    def view_enrolment(self, student: Student):
        Color.prYellow(f"Showing {len(student.enrolment)} subjects")
        if student.enrolment:
            for subject in student.enrolment:
                print(f"[ {subject.__str__()} ]")

    def remove_subject(self):
        removesubjectbyid = input("Remove Subject by ID: ")

        return removesubjectbyid
