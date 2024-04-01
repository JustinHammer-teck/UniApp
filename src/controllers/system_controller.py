from models import admin


class SystemController:
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

    @classmethod
    def login(cls, user: str, password: str):
        pass

    @classmethod
    def login_admin(cls):
        pass

    def __assign_id(self) -> int:
        for i in range(0, 5):
            for k in range(0, i):
                print()

        return 0

    def system_menu(self):
        pass
