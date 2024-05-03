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
            Color.prRed(f"Student {student_id} does not exist")
            return
        self.db.context.remove(student[0])
        self.db.save()
        Color.prYellow(f"Removing Student {student_id} account")

    def clear_database(self):
        user_confirmation = self.view.clear_database()
        if user_confirmation:
            self.db.clear()
            Color.prGreen("Successfully Clear All Data")

    def __add_grade_groups(self, grade, student_info, grade_groups):
        if grade not in grade_groups:
            grade_groups[grade] = []

        grade_groups[grade].append(student_info)

    def __form_grade_groups(self, students):
        grade_groups = {}
        for student in students:
            for subject in student.enrolment:
                info = f"{student.name} :: {student.id} --> GRADE:  {subject.grade} - MARK: {subject.mark}"
                self.__add_grade_groups(subject.grade, info, grade_groups)
        return grade_groups
