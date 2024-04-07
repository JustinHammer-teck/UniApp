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
            Color.prCyan("4. [E]xit")
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
                case "4" | "e":
                    self.exit()
                    break

    def admin_menu(self):
        while True:
            Color.prCyan("1. [V]iew All Students")
            Color.prCyan("2. [G]roup Students")
            Color.prCyan("3. [P]artition Students")
            Color.prCyan("4. [R]emove Student")
            Color.prCyan("5. [C]lear File")
            Color.prCyan("6. [L]ogout")
            Color.prCyan("7. [Q]uit")
            Color.prCyan("==========================")

            userchoice = input("User can choose either [Number] or the [First Letter]: ")

            match userchoice.lower():
                case "1" | "v":
                    pass
                case "2" | "g":
                    pass
                case "3" | "p":
                    pass
                case "4" | "r":
                    pass
                case "5" | "c":
                    pass
                case "6" | "l":
                    self.__logout()
                    break
                case "7" | "q":
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
            Color.prCyan("6. [C]hange Password")
            Color.prCyan("7. [L]ogout")
            Color.prCyan("8. [Q]uit")            
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
                case "6" | "c":
                    pass
                case "7" | "l":
                    self.__logout()
                    break
                case "8" | "q":
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

# import os
# import platform
#
# # Global variables
# current_menu = 'main'
# messages = []  # A list to hold messages to be displayed
#
# def clear_screen():
#     """Clears the console screen."""
#     if platform.system() == "Windows":
#         os.system('cls')
#     else:
#         os.system('clear')
#
# def add_message(message):
#     """Adds a message to the messages list."""
#     global messages
#     messages.append(message)
#
# def display():
#     """Handles the display update, showing messages and the current menu."""
#     clear_screen()
#     for message in messages:
#         print(message)
#     messages.clear()  # Clear messages after displaying
#
#     if current_menu == 'main':
#         show_main_menu()
#     elif current_menu == 'submenu':
#         show_submenu()
#
# def view_predefined_context():
#     add_message("\nHello World")
#
# def input_and_print():
#     user_input = input("\nEnter something: ")
#     add_message(f"You entered: {user_input}")
#
# def show_main_menu():
#     print("\nMain Menu:")
#     print("1. View predefined context")
#     print("2. Input something and print it")
#     print("3. Open sub-menu example")
#     print("4. Exit")
#
# def show_submenu():
#     print("\nSub-Menu:")
#     print("1. Say Hello")
#     print("2. Say Goodbye")
#     print("3. Return to main menu")
#
# def handle_submenu_choice(choice):
#     global current_menu
#     if choice == '1':
#         add_message("\nHello from the sub-menu!")
#     elif choice == '2':
#         add_message("\nGoodbye from the sub-menu!")
#     elif choice == '3':
#         current_menu = 'main'
#     else:
#         add_message("Invalid option, please try again.")
#
# def main():
#     global current_menu
#
#     while True:
#         display()  # Update display at the start of each loop
#
#         choice = input("Choose an option: ")
#
#         if current_menu == 'main':
#             if choice == '1':
#                 view_predefined_context()
#             elif choice == '2':
#                 input_and_print()
#             elif choice == '3':
#                 current_menu = 'submenu'
#             elif choice == '4':
#                 add_message("Exiting...")
#                 display()  # Final display update to show exit message
#                 break
#             else:
#                 add_message("Invalid option, please try again.")
#         elif current_menu == 'submenu':
#             handle_submenu_choice(choice)
#
# if __name__ == "__main__":
#     main()
