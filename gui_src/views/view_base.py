from tkinter import ttk
from cores.view import View


class ViewBase(ttk.Frame, View):
    def __init__(self, core):
        super().__init__()
        self.core = core
