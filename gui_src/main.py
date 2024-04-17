#!/bin/zsh

import tkinter as tk

from cores.default_layout import DefaultLayout
from cores.core import Core


class GuiUniApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")

    def main(self):
        Core(self).controller("home")


if __name__ == "__main__":
    app = GuiUniApp()
    app.main()
    app.mainloop()
