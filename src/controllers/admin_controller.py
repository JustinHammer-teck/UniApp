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
        pass

    def view_by_passfail(self):
        pass

    def remove_student(self, student_id: str):
        pass

    def clear_database(self):
        user_confirmation = self.view.clear_database()
        if user_confirmation:
            self.db.clear()
            Color.prGreen("Successfully Clear All Data")
