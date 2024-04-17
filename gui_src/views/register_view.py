from tkinter import ttk

from cores.view import View
from cores.default_layout import DefaultLayout
from cores.core import Core


class Register(ttk.Frame, View):
    def __init__(self):
        super().__init__()
        self.layout = DefaultLayout()
        self.controller = Core().controller("student")
