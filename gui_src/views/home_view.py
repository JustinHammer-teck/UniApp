from tkinter import NSEW, ttk

from cores.view import View
from cores.core import Core


class HomeView(ttk.Frame, View):
    def __init__(self, layout, core: Core) -> None:
        self.layout = layout.main()

        super().__init__(self.layout.application)

        self.core = core

    def main(self):
        ttk.Button(
            self,
            text="Hola from the home view",
            command=lambda: self.core.controller("home", "hello"),
        ).grid(row=1, column=0, sticky=NSEW)

        ttk.Button(
            self,
            text="Suck",
            command=lambda: self.core.controller("home", "hello"),
        ).grid(row=1, column=1, sticky=NSEW)

        self.grid(row=1, column=0, rowspan=2, padx=10, pady=10)

    def close(self):
        return
