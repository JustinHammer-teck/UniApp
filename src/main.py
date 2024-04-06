from os import system, name
import sys

from models.admin import Admin
from models.student import Student
from controllers import admin_controller as admin_ctrl
from controllers import student_controller as stu_ctrl


class UniApp:
    notifications: str
    session: Student | Admin | None

    def __init__(self) -> None:
        self.notifications = ""
        self.session = None
        self.menu = None

    def main(self):
        while True:
            if type(self.session) is Admin:
                self.admin_menu()
            elif type(self.session) is Student:
                self.student_menu()
            else: 
                self.default_menu()

    def default_menu(self):
        while True:
            self.clear()
            print("1. Login Student")
            print("2. Login Admin")
            print("3. Register")
            print("4. Exit")
            self.__notify_if_any()

            userchoice = int(input("choose: "))
 
            match userchoice:
                case 1:
                    (student, msg) = stu_ctrl.StudentController().login()
                    if not msg:
                        self.session = student
                        self.notifications = ""
                    else:
                        self.notifications = msg
                    break
                case 2:
                    self.session = Admin()
                    break
                case 3:
                    msg = stu_ctrl.StudentController().register()
                    self.notifications = msg
                    break
                case 4:
                    self.exit()
                    break

    def admin_menu(self):
        while True:
            self.clear()
            print("3. Logout")
            print("4. Quit")
            self.__notify_if_any()

            userchoice = int(input("choose: "))

            match userchoice:
                case 3:
                    self.__logout()
                    break
                case 4:
                    self.exit()
                    break

    def student_menu(self):
        while True:
            if self.session is not Student:
                break

            self.clear()
            print("1. Enrol New Subject")
            print("2. Remove Subject")
            print("3. View My Enrolment")
            print("4. Subject Result")
            print("5. Session Result")
            print("6. Change Password")
            print("7. Logout")
            print("8. Quit")
            self.__notify_if_any()

            if self.session:
                print(f"Hello \n{self.session.__str__()}")

            userchoice = int(input("choose: "))

            match userchoice:
                case 1:
                    stu_ctrl.StudentController().enrol_subject(self.session)
                    break
                case 2:
                    stu_ctrl.StudentController().remove_subject(self.session)
                    break
                case 7:
                    self.__logout()
                    break

    def __logout(self):
        self.notifications = ""
        self.session = None

    def __notify_if_any(self):
        if self.notifications:
            print(self.notifications)
            self.__reset_notification()

    def __reset_notification(self):
        self.notifications = ""

    @staticmethod
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    @staticmethod
    def exit():
        sys.exit()

if __name__ == "__main__":
    UniApp().main()
