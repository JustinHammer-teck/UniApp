from cores.controller import Controller
from views.admin_review import AdminView


class AdminController(Controller):
    def __init__(self) -> None:
        super().__init__()
        self.view = AdminView()

    def admin_login(self):
        pass

    def get_students(self):
        pass

    def clear_data(self):
        pass

    def group_students(self):
        pass

    def partition_student(self):
        pass

    def remove_student(self):
        pass

    def main(self):
        self.view.main()
