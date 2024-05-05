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
            Color.prYellow("There is no student yet")

    def view_by_grade(self, grades_dict: dict):
        Color.prYellow("Grade Grouping")
        if grades_dict:
            for grades, students in grades_dict.items():
                print(f"{grades}:", end=" --> ")
                print(f"[{', '.join(students)}]")
        else:
            Color.prYellow("There is no student yet")

    def view_by_passfail(self, grades_dict: dict):
        Color.prYellow("PASS/FAIL Partition")
        if grades_dict:
            if grades_dict["Z"]:
                print("FAIL", end=" --> ")
                print(f"[{', '.join(grades_dict['Z'])}]")
            else:
                print("FAIL --> []")
            print("PASS", end=" --> ")
            pass_grades_info = ", ".join(
                [
                    f"{', '.join(students)}"
                    for grade, students in grades_dict.items()
                    if grade != "Z"
                ]
            )
            print(f"[{pass_grades_info}]")
        else:
            Color.prYellow("There is no student yet")

    def clear_database(self) -> bool:
        Color.prYellow("Clearing students database")
        user_choice = input(
            "\033[91m Are You Sure To Delete All Student Data ? [Y] yes or [N] no: \033[00m"
        )

        return True if user_choice.lower() == "y" else False
