from persistent.db import Database
from views.admin_view import AdminView


class AdminController:

    def __init__(self) -> None:
        self.db = Database()
        self.view = AdminView()

    def view_students(self):
        pass

    def view_by_grade(self):
        pass

    def view_by_passfail(self):
        pass

    def remove_student(self, student_id: str):
        pass

    def clear_database(self):
        self.db.clear()
