from tkinter import NSEW, ttk

from cores.view import View
from cores.core import Core
from cores.default_layout import DefaultLayout


class HomeView(ttk.Frame, View):
    def __init__(self, core: Core) -> None:
        self.core = core
        self.core.root.title("Student View")
        self.layout = DefaultLayout(self.core.root)

        super().__init__(self.layout.application)

    def main(self):
        ttk.Button(
            self,
            text="Hola from the home view",
            command=lambda: self.core.controller("home", "hello"),
        ).grid(row=0, column=0, sticky=NSEW)

        ttk.Button(
            self,
            text="Suck",
            command=lambda: self.core.controller("home", "hello"),
        ).grid(row=0, column=1, sticky=NSEW)

        self.grid(row=1, column=0, rowspan=2, padx=10, pady=10)
        self.layout.main()

    def close(self):
        self.layout.application.destroy()
        self.layout.menu.destroy()
        self.destroy()
