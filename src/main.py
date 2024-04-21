from os import system, name
import sys

from common.color import Color
from models.admin import Admin
from models.student import Student
from controllers import admin_controller as admin_ctrl
from controllers import student_controller as stu_ctrl


class UniApp:
    session: Student | Admin | None

    def __init__(self) -> None:
        self.session = None

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
            Color.prCyan("1. [L]ogin [S]tudent")
            Color.prCyan("2. [L]ogin [A]dmin")
            Color.prCyan("3. [R]egister")
            Color.prCyan("4. [C]lear")
            Color.prCyan("5. [E]xit")
            Color.prCyan("==========================")

            userchoice = input("User can choose either [Number] or the [First Letter]: ")

            match userchoice.lower():
                case "1" | "ls":
                    self.session = stu_ctrl.StudentController().login()
                    break
                case "1" | "la":
                    self.session = Admin()
                    break
                case "3" | "r":
                    stu_ctrl.StudentController().register()
                    break
                case "4" | "c":
                    self.clear()
                case "5" | "e":
                    Color.prYellow("Exit")
                    self.exit()
                    break

    def admin_menu(self):
        while True:
            Color.prCyan("1. [V]iew All Students")
            Color.prCyan("2. [G]roup Students")
            Color.prCyan("3. [P]artition Students")
            Color.prCyan("4. [R]emove Student")
            Color.prCyan("5. [C]lear [D]ata")
            Color.prCyan("6. [C]lear")
            Color.prCyan("7. [L]ogout")
            Color.prCyan("8. [Q]uit")
            Color.prCyan("==========================")

            userchoice = input("User can choose either [Number] or the [First Letter]: ")

            match userchoice.lower():
                case "1" | "v":
                    admin_ctrl.AdminController().view_students()
                case "2" | "g":
                    pass
                case "3" | "p":
                    pass
                case "4" | "r":
                    pass
                case "5" | "cd":
                    admin_ctrl.AdminController().clear_database()
                case "6" | "c":
                    self.clear()
                case "7" | "l":
                    self.__logout()
                    break
                case "8" | "q":
                    Color.prYellow("Exit")
                    self.exit()
                    break

    def student_menu(self):
        while True:

            if type(self.session) is not Student:
                break

            Color.prCyan("1. [E]nrol New Subject")
            Color.prCyan("2. [R]emove Subject")
            Color.prCyan("3. [V]iew My Enrolment")
            Color.prCyan("4. [S]ubject Result")
            Color.prCyan("5. [Se]ssion Result")
            Color.prCyan("6. [C]hange [P]assword")
            Color.prCyan("7. [C]lear")
            Color.prCyan("8. [L]ogout")
            Color.prCyan("9. [Q]uit")            
            Color.prCyan("==========================")

            if self.session:
                Color.prYellow(f"Hello \n{self.session.__str__()}")

            userchoice = input("User can choose either [Number] or the [First Letter]: ")

            match userchoice.lower():
                case "1" | "e":
                    stu_ctrl.StudentController().enrol_subject(self.session)
                case "2" | "r":
                    stu_ctrl.StudentController().remove_subject(self.session)
                case "3" | "v":
                    stu_ctrl.StudentController().view_enrolment(self.session)
                case "4" | "s":
                    pass
                case "5" | "se":
                    pass
                case "6" | "cp":
                    stu_ctrl.StudentController().change_password(self.session)
                case "7" | "c":
                    self.clear()
                case "8" | "l":
                    self.__logout()
                    break
                case "9" | "q":
                    Color.prYellow("Exit")
                    self.exit()
                    break


    def __logout(self):
        self.session = None

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
