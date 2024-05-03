from tkinter import ttk

from cores.core import Core
from cores.view import View
from cores.single_layout import SingleLayout


class AuthView(ttk.Frame, View):
    def __init__(self, core: Core) -> None:
        self.core = core
        self.core.root.title("Student Login")
        self.layout = SingleLayout(self.core.root)

        super().__init__(self.layout.application)

    def main(self):
        ttk.Label(self, text="Email:").grid(
            row=1, column=0, padx=10, pady=5, sticky="e"
        )
        self.email_entry = ttk.Entry(self, width=30)
        self.email_entry.grid(row=1, column=1, padx=10, pady=5)

        # Create password label and entry
        ttk.Label(self, text="Password:").grid(
            row=2, column=0, padx=10, pady=5, sticky="e"
        )
        self.password_entry = ttk.Entry(self, show="*", width=30)
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)

        # Create login button
        ttk.Button(
            self,
            text="Login",
            command=lambda: self.core.controller(
                "auth",
                "login",
                username=self.email_entry.get(),
                password=self.password_entry.get(),
            ),
        ).grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.grid(row=0, column=0, rowspan=2, padx=10, pady=10)
        self.layout.main()

    def close(self):
        self.destroy()
