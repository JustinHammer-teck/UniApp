from tkinter import ttk


class DefaultLayout:
    def __init__(self, root):

        ttk.Label(master=root, anchor="center", text="GuiUniAPP").grid(
            row=0, column=0, columnspan=2, padx=10, pady=10, sticky="NE"
        )

        self.application = ttk.Frame(master=root, width=200, height=400)
        self.menu = ttk.Frame(master=root, width=650, height=400)

    def main(self):
        ttk.Button(self.menu, text="Enrol Subject").pack(padx=15, pady=10)
        ttk.Button(self.menu, text="Remove Subject").pack(padx=15, pady=10)
        ttk.Button(self.menu, text="View Subject Info").pack(padx=15, pady=10)
        ttk.Button(self.menu, text="Exit").pack(padx=15, pady=10)

        self.menu.grid(row=1, column=0, padx=10, pady=5)
        self.application.grid(row=1, column=1, columnspan=2, padx=10, pady=5)
        return self
