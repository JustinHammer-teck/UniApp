from typing import List
from common.color import Color
from models.student import Student


class AdminView:
    def remove_student(self):
        pass

    def view_students(self, students: List[Student]):
        Color.prYellow("Student List")
        if students:
            for student in students:
                print(student.__str__())
        else:
            Color.prYellow("There is no student yet")

    def view_by_grade(self):
        pass

    def view_by_passfail(self):
        pass

    def clear_database(self) -> bool:

        user_choice = input(
            "\033[91m Are You Sure To Delete All Student Data ? [Y] yes or [N] no: \033[00m"
        )

        return True if user_choice.lower() == "y" else False
