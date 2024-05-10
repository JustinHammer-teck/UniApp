import tkinter as tk
import tkinter.messagebox as tkmb
from tkinter import ttk

from gui.cores.core import Core
from gui.cores.view import View
from gui.layouts.default_layout import DefaultLayout


class HomeView(ttk.Frame, View):
    def __init__(self, core: Core) -> None:
        self.core = core
        self.core.root.title("Student View")
        self.layout = DefaultLayout(self.core.root).main()

        super().__init__(self.layout.application)

    def main(self):
        self.focus_force()
        self.grid(row=1, column=0, rowspan=2)
        self.application()
        self.menu()

    def application(self):
        self.tree = ttk.Treeview(
            self,
            columns=("Subject ID", "Subject Name", "Mark", "Grade"),
            show="headings",
        )

        self.tree.heading("Subject ID", text="Subject ID")
        self.tree.heading("Subject Name", text="Subject Name")
        self.tree.heading("Mark", text="Mark")
        self.tree.heading("Grade", text="Grade")

        subjects = self.core.controller(
            "home", "get_subjects", student_id=self.core.user.id
        )
        if subjects:
            for subject in subjects:
                self.tree.insert(
                    "",
                    "end",
                    values=(subject.id, subject.name, subject.mark, subject.grade),
                )

        self.tree.pack(expand=True, fill="both")

    def menu(self):
        tk.Button(
            self.layout.menu,
            text="Enrol Subject",
            command=lambda: self.core.controller(
                "home", "enrol_subject", student_id=self.core.user.id
            ),
        ).pack(padx=15, pady=10)
        tk.Button(
            self.layout.menu,
            text="Remove Subject",
            command=lambda: self.__delete_selected(),
        ).pack(padx=15, pady=10)
        tk.Button(
            self.layout.menu,
            text="Log Out",
            command=lambda: self.__logout_confirm(),
        ).pack(padx=15, pady=10)

    def __delete_selected(self):
        curItem = self.tree.focus()
        if curItem:
            subject_id = self.tree.item(curItem)["values"][0]
            self.core.controller(
                "home",
                "remove_subject",
                student_id=self.core.user.id,
                subject_id=subject_id,
            )

    def __logout_confirm(self):
        answer = tkmb.askyesno(
            title="confirmation", message="Are you sure that you want to quit?"
        )
        if answer:
            return self.core.controller("auth", "logout")

    def close(self):
        self.layout.close()
        self.destroy()
