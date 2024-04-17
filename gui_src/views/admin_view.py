import tkinter as tk

from gui_src.controllers.admin_controller import AdminController
from gui_src.cores.view import View


class AdminView(tk.Tk, View):
    def __init__(self) -> None:
        super().__init__()
        self.controller = AdminController()

    def main(self):
        self.mainloop()

    def close(self):
        return
