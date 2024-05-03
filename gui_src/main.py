#!/bin/zsh

import tkinter

from cores.core import Core


class GuiUniApp(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("850x400")

    def main(self):
        Core(self).controller("auth")


if __name__ == "__main__":
    app = GuiUniApp()
    app.main()
    app.mainloop()
