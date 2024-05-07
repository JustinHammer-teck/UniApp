from cores.controller import Controller
from cores.core import Core


class AuthController(Controller):
    def __init__(self, core: Core) -> None:
        super().__init__()
        self.core = core

    def login(self, username: str, password: str):
        print(username)
        self.core.controller("home")

    def logout(self):
        self.core.logout()
        return self.core.controller("auth")

    def main(self):
        self.view
