import tkinter as tk

from gui_src.controllers.home_controller import HomeController
from gui_src.cores.view import View


class HomeView(tk.Tk, View):
    def __init__(self) -> None:
        super().__init__()
        self.controller = HomeController()

    def main(self):
        self.mainloop()

    def close(self):
        return
