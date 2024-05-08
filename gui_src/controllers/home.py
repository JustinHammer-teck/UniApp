from cores.controller import Controller


class HomeController(Controller):
    def __init__(self, core) -> None:
        super().__init__()
        self.core = core

    def hello(self):
        print("Hello World")

    def main(self):
        self.view
