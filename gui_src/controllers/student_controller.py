from gui_src.cores.controller import Controller
from gui_src.views.student_view import StudentView


class StudentController(Controller):
    def __init__(self) -> None:
        super().__init__()
        self.view = StudentView()

    def student_login(self):
        pass

    def enrol_subject(self):
        pass

    def view_enrolment(self):
        pass

    def remove_enrolment(self):
        pass

    def change_password(self):
        pass

    def main(self):
        self.view.main()
