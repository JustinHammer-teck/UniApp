from os import system, name
from typing import List

from src.controllers import admin_controller as adminctrl
from src.controllers import student_controller as stuctrl


class Sumthing:
    name: str
    id: int
    mores: List[str]

    def __init__(self, name, id, mores) -> None:
        self.name, self.id, self.mores = name, id, mores

    def __str__(self) -> str:
        return f"Name: {self.name} \nId: {self.id} \nMores: {self.mores}"


class UniApp:
    error_msg: str
    
    def __init__(self) -> None:
        self.error_msg = ""

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
                    (is_auth, msg) = stuctrl.StudentController().login()
                    if is_auth:
                        self.student_menu()
                        self.error_msg = ""
                    else:
                        self.error_msg = msg
                case 2:
                    self.admin_menu()
                case 3:
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
 
    # sys = Sys()
    # for i in range(1, 15):
    #     sys.add(Sumthing("HI", i, ["Sumethin", "is", "awesome"]))
    #
    # file = open("./students.data", "wb")
    #
    # pickle.dump(sys, file)
    #
    # file.close()
    #
    # try:
    #     newsys = Sys()
    #     with open("./students.data", "rb") as file:
    #         newsys = pickle.load(file)
    #
    #     file.close()
    #     for i in newsys.value:
    #         print(i.__str__())
    #
    # except Exception as e:
    #     print(str(e))


if __name__ == "__main__":
    UniApp().main()
