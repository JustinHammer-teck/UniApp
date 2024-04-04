from os import system, name

from src.persistent.db import Database
from src.models.admin import Admin
from src.models.student import Student
from src.controllers import admin_controller as admin_ctrl
from src.controllers import student_controller as stu_ctrl


class UniApp:
    error_msg: str
    student_session: Student | None

    def __init__(self) -> None:
        self.error_msg = ""
        self.student_session = None
        self.menu = None

    def main(self):
        while True:
            self.clear()
            print("1. Login Student")
            print("2. Login Admin")
            print("3. Register")
            print("4. Exit")

            userchoice = int(input("choose: "))

            if self.error_msg:
                print(self.error_msg)

            if self.student_session:
                print(f"Hello \n{self.student_session.__str__()}")

            match userchoice:
                case 1:
                    (student, msg) = stu_ctrl.StudentController().login()
                    if not msg:
                        self.student_session = student
                        self.error_msg = ""

                        self.student_menu()
                    else:
                        self.error_msg = msg
                case 2:
                    self.admin_menu()
                case 3:
                    stu_ctrl.StudentController().register()
                case 4:
                    break

    def admin_menu(self):
        while True:
            self.clear()
            print("3. Exit")

    def student_menu(self):
        while True:
            self.clear()
            print("1. Enrol New Subject")
            print("2. Remove Subject")
            print("3. View My Enrolment")
            print("4. Change Password")
            print("5. Exit")
            userchoice = int(input("choose: "))

            if self.student_session is None:
                break

            match userchoice:
                case 1:
                    stu_ctrl.StudentController().enrol_subject(self.student_session)
                case 2:
                    stu_ctrl.StudentController().remove_subject(self.student_session)

    @staticmethod
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

if __name__ == "__main__":
    UniApp().main()
