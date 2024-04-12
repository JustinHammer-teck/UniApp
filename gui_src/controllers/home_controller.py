from gui_src.cores.controller import Controller
from gui_src.cores.view import View
from gui_src.views.home_view import HomeView


class HomeController(Controller):
    view: View

    def __init__(self) -> None:
        super().__init__()
        self.view = HomeView()

    def admin_menu(self):
        pass

    def student_menu(self):
        pass

    def main(self):
        self.view.main()
