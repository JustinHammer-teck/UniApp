from cores.controller import Controller
from cores.core import Core


class AuthController(Controller):
    def __init__(self, core: Core) -> None:
        super().__init__()
        self.core = core

    def login(self, username: str, password: str):
        print(username)
        return self.core.controller("home")

    def main(self):
        self.view
