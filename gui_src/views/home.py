from tkinter import NSEW, ttk
import tkinter as tk
from tkinter.messagebox import askyesno
from cores.view import View
from cores.core import Core
from layouts.default_layout import DefaultLayout


class HomeView(ttk.Frame, View):
    def __init__(self, core: Core) -> None:
        self.core = core
        self.core.root.title("Student View")
        self.layout = DefaultLayout(self.core.root).main()

        super().__init__(self.layout.application)
        tk.Button(
            self,
            text="Hola from the home view",
            command=lambda: self.core.controller("home", "hello"),
        ).grid(row=0, column=0, sticky=NSEW)

        tk.Button(
            self,
            text="Suck",
            command=lambda: self.core.controller("home", "hello"),
        ).grid(row=0, column=1, sticky=NSEW)

    def main(self):
        self.focus_force()
        self.grid(row=1, column=0, rowspan=2)
        self.menu()

    def menu(self):
        tk.Button(self.layout.menu, text="Enrol Subject").pack(padx=15, pady=10)
        tk.Button(self.layout.menu, text="Remove Subject").pack(padx=15, pady=10)
        tk.Button(self.layout.menu, text="View Subject Info").pack(padx=15, pady=10)
        tk.Button(
            self.layout.menu, text="Log Out", command=lambda: self.logout_confirm()
        ).pack(padx=15, pady=10)

    def logout_confirm(self):
        answer = askyesno(
            title="confirmation", message="Are you sure that you want to quit?"
        )
        if answer:
            return self.core.controller("auth", "logout")

    def close(self):
        self.layout.close()
        self.destroy()
