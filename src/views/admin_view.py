from typing import List
from common.color import Color
from models.student import Student


class AdminView:
    def remove_student(self):
        id = input("Remove by ID: ")
        return id

    def view_students(self, students: List[Student]):
        Color.prYellow("Student List")
        if students:
            for student in students:
                print(student.__str__())
        else:
            print("\t< Nothing to Display >")

    def view_by_grade(self, grades_dict: dict):
        Color.prYellow("Grade Grouping")
        if grades_dict:
            for grades, student_info in grades_dict.items():
                print(f"{grades}:", end=" --> ")
                print(f"[{', '.join(student_info)}]")
        else:
            print("\t< Nothing to Display >")

    def view_by_passfail(self, grades_dict: dict):
        Color.prYellow("PASS/FAIL Partition")
        if grades_dict:
            if "Z" not in grades_dict:
                print("FAIL --> []")
            else:
                print("FAIL", end=" --> ")
                print(f"[{', '.join(grades_dict['Z'])}]")
            print("PASS", end=" --> ")
            pass_grades_info = ", ".join(
                [
                    f"{', '.join(student_info)}"
                    for grade, student_info in grades_dict.items()
                    if grade != "Z"
                ]
            )
            if not pass_grades_info:
                print("[]")
            else:
                print(f"[{pass_grades_info}]")
        else:
            print("\t< Nothing to Display >")

    def clear_database(self) -> bool:
        Color.prYellow("Clearing students database")
        user_choice = input(
            "\033[91m Are You Sure To Delete All Student Data ? [Y] yes or [N] no: \033[00m"
        )

        return True if user_choice.lower() == "y" else False
