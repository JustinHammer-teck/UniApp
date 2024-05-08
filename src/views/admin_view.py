from typing import List
from common.color import Color
from models.student import Student


class AdminView:
    def remove_student(self):
        id = input("\tRemove by ID: ")
        return id

    def view_students(self, students: List[Student]):
        Color.prYellow("\tStudent List")
        if students:
            for student in students:
                print("\t" + student.__str__())
        else:
            Color.prYellow("\tThere is no student yet")

    def view_by_grade(self, grades_dict: dict):
        Color.prYellow("\tGrade Grouping")
        if grades_dict:
            for grades, students in grades_dict.items():
                print(f"\t{grades}:", end=" --> ")
                print(f"[{', '.join(students)}]")
        else:
            Color.prYellow("\tThere is no student yet")

    def view_by_passfail(self, grades_dict: dict):
        Color.prYellow("\tPASS/FAIL Partition")
        if grades_dict:
            if grades_dict["Z"]:
                print("\tFAIL", end=" --> ")
                print(f"[{', '.join(grades_dict['Z'])}]")
            else:
                print("\tFAIL --> []")
            print("\tPASS", end=" --> ")
            pass_grades_info = ", ".join(
                [
                    f"{', '.join(students)}"
                    for grade, students in grades_dict.items()
                    if grade != "Z"
                ]
            )
            print(f"\t[{pass_grades_info}]")
        else:
            Color.prYellow("\tThere is no student yet")

    def clear_database(self) -> bool:
        Color.prYellow("\tClearing students database")
        user_choice = input(
            "\t\033[91m Are You Sure To Delete All Student Data ? [Y] yes or [N] no: \033[00m"
        )

        return True if user_choice.lower() == "y" else False
