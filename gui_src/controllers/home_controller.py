from cores.controller import Controller
from cores.core import Core


class HomeController(Controller):
    def __init__(self, core) -> None:
        super().__init__()
        self.root = core.root
        self.view = self.view("Home")

    def admin_menu(self):
        pass

    def student_menu(self):
        pass

    def main(self):
        self.view.main()
        self.view.layout.pack()
