#!/bin/zsh

import tkinter

from gui.cores.core import Core


class GuiUniApp(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg="#003C43")  # Set background color of root window

    def main(self):
        Core(self).controller("auth")
