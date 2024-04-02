from typing import List

from src.controllers.admin_controller import AdminController
from src.controllers.student_controller import StudentController


class Sumthing:
    name: str
    id: int
    mores: List[str]

    def __init__(self, name, id, mores) -> None:
        self.name, self.id, self.mores = name, id, mores

    def __str__(self) -> str:
        return f"Name: {self.name} \nId: {self.id} \nMores: {self.mores}"


class Sys:
    value: List[Sumthing]

    def __init__(self) -> None:
        self.value = []

    def add(self, sum: Sumthing):
        self.value.append(sum)


def admin_menu():
    while True:
        print("1. Add Student")
        print("2. Do something in admin")
        print("3. Exit")

def student_menu():
    print("1. Do something in student")
    print("2. Exit")
    userchoice = int(input("choose: "))
    while True:
        match userchoice:
            case 1:
                print("Awesome")

def main():
    while True:
        print("1. Login Student")
        print("2. Login Admin")
        print("3. Exit")
        userchoice = int(input("choose: "))

        match userchoice:
            case 1:
                if StudentController().login():
                    student_menu()
            case 2:
                AdminController()
                admin_menu()

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
    main()
