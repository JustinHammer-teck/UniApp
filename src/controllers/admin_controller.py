from ..persistent.db import Database
from ..views.admin_view import AdminView


class AdminController:

    def __init__(self) -> None:
        self.db = Database()
        self.view = AdminView()

    def clear_database(self):
        self.db.clear()
