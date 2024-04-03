from os import system, name

from src.models.admin import Admin
from src.models.student import Student
from src.controllers import admin_controller as admin_ctrl
from src.controllers import student_controller as stu_ctrl


class UniApp:
    error_msg: str
    current_session: Student | Admin | None

    def __init__(self) -> None:
        self.error_msg = ""
        self.current_session = None

    def main(self):
        while True:
            self.clear()
            if self.error_msg:
                print(self.error_msg)

            print("1. Login Student")
            print("2. Login Admin")
            print("3. Register")
            print("4. Exit")

            userchoice = int(input("choose: "))

            match userchoice:
                case 1:
                    (student, msg) = stu_ctrl.StudentController().login()
                    if msg:
                        self.current_session = student
                        self.student_menu()
                        self.error_msg = ""
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
            print("1. Add Student")
            print("2. Do something in admin")
            print("3. Exit")

    def student_menu(self):
        while True:
            self.clear()
            print("1. Get enrolment list")
            print("2. Enrol subject")
            print("2. Enrol subject")
            print("2. Enrol subject")
            userchoice = int(input("choose: "))
            match userchoice:
                case 1:
                    print("Awesome")
    
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
    # students : List[Student] = []
    #
    # for i in range(1 ,10):
    #     students.append(Student(i.__str__(), f"halo{i}", f"halo{i}@", "123"))
    #
    # db = db.Database()
    # db.context = students
    #
    # db.save()
    #
    # data = db.read()
    #
    # for i in data:
    #     print(i.__str__())
