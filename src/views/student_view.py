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
<<<<<<< HEAD
        pass
=======
        print(subject.__str__())
>>>>>>> be6b92d (UniApp: finished implement for menu control flow)

    def view_enrolment(self, student: Student):
        if student.enrolment:
            for subject in student.enrolment:
                print(subject.__str__())
        else:
            print("Student do not enrol any subject yet")

    def remove_subject(self, student: Student):
        pass
