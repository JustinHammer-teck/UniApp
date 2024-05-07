#!/bin/zsh

import tkinter

from cores.core import Core


class GuiUniApp(tkinter.Tk):
    def __init__(self):
        super().__init__()
        # self.geometry("550x400")
        self.configure(bg="#003C43")  # Set background color of root window

    def main(self):
        Core(self).controller("auth")


if __name__ == "__main__":
    app = GuiUniApp()
    app.main()
    app.mainloop()
