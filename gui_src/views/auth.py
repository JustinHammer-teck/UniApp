import tkinter as tk

from cores.core import Core
from cores.view import View
from layouts.single_layout import SingleLayout


class AuthView(tk.Frame, View):
    def __init__(self, core: Core) -> None:
        self.core = core
        self.layout = SingleLayout(self.core.root).main()
        super().__init__(self.layout.application)

        self.configure(bg="#003C43")  # Set background color

        fg_color = "#E3FEF7"

        self.core.root.title("Student Login")

        tk.Label(self, text="Email:", bg="#003C43", fg=fg_color).grid(
            row=1, column=0, padx=10, pady=5, sticky="e"
        )
        self.email_entry = tk.Entry(self, width=30)

        tk.Label(self, text="Password:", bg="#003C43", fg=fg_color).grid(
            row=2, column=0, padx=10, pady=5, sticky="e"
        )
        self.password_entry = tk.Entry(self, show="*", width=30)

        # Login button
        tk.Button(
            self,
            text="Login",
            command=lambda: self.core.controller(
                "auth",
                "login",
                username=self.email_entry.get(),
                password=self.password_entry.get(),
            ),
            bg="#135D66",  # Set button background color
            fg=fg_color,  # Set button foreground color
        ).grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def main(self):
        self.focus_force()
        self.email_entry.grid(row=1, column=1, padx=10, pady=5)
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)
        self.grid(row=0, column=0, rowspan=2, padx=10, pady=10)

    def close(self):
        self.layout.close()
        self.destroy()
