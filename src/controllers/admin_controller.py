from ..models.db import Database
from ..views.admin_view import AdminView


class AdminController:

    def __init__(self) -> None:
        self.db = Database()
        self.view = AdminView()

        self.__load_student()

    def __load_student(self):
        self.db.read()
