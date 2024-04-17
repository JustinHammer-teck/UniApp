from tkinter import NSEW, ttk
from cores.core import Core
from gui_src.cores.view import View


class HomeView(ttk.Frame, View):
    def __init__(self, layout) -> None:
        self.layout = layout

    def main(self):
        ttk.Button(self.layout, text="Holad from the home view").grid(
            row=0, column=0, sticky=NSEW
        )

        return self.layout

    def close(self):
        return
