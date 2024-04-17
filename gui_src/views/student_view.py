import tkinter as tk

from controllers.student_controller import StudentController
from cores.view import View


class StudentView(tk.Tk, View):
    def __init__(self) -> None:
        super().__init__()
        self.controller = StudentController()

    def main(self):
        self.mainloop()

    def close(self):
        return
