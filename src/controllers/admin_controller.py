from common.color import Color
from persistent.db import Database
from views.admin_view import AdminView


class AdminController:
    def __init__(self) -> None:
        self.db = Database()
        self.view = AdminView()

    def view_students(self):
        students = self.db.read()
        self.view.view_students(students)

    def view_by_grade(self):
        grade_groups = self.__form_grade_groups(self.db.read())
        self.view.view_by_grade(grade_groups)

    def view_by_passfail(self):
        grade_groups = self.__form_grade_groups(self.db.read())
        self.view.view_by_passfail(grade_groups)

    def remove_student(self):
        student_id = self.view.remove_student()
        students = self.db.read()
        student = [student for student in students if student.id == student_id]

        if not student:
            Color.prRed(f"\tStudent {student_id} does not exist")
            return
        self.db.context.remove(student[0])
        self.db.save()
        Color.prYellow(f"\tRemoving Student {student_id} account")

    def clear_database(self):
        user_confirmation = self.view.clear_database()
        if user_confirmation:
            self.db.clear()
            Color.prYellow("\tStudents data cleared")

    def __add_grade_groups(self, grade, student_info, grade_groups):
        if grade not in grade_groups:
            grade_groups[grade] = []

        grade_groups[grade].append(student_info)

    def __form_grade_groups(self, students):
        grade_groups = {}
        for student in students:
            if student.average_score() == -1:
                continue
            average_grade = self.letter_marks(student.average_score())
            info = f"{student.name} :: {student.id} --> GRADE:  {average_grade} - MARK: {student.average_score()}"
            self.__add_grade_groups(average_grade, info, grade_groups)
        return grade_groups

    def letter_marks(self, mark: int):
        if mark < 50:
            return "Z"
        elif 50 <= mark < 65:
            return "P"
        elif 65 <= mark < 75:
            return "C"
        elif 75 <= mark < 85:
            return "D"
        elif mark >= 85:
            return "HD"
