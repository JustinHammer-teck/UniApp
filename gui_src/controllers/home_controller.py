from cores.controller import Controller
from cores.view import View


class HomeController(Controller):
    view: View

    def __init__(self) -> None:
        super().__init__()

    def admin_menu(self):
        pass

    def student_menu(self):
        pass

    def hello(self):
        print("Hello World")

    def set_view(self, view):
        self.view = view

    def main(self):
        self.view
