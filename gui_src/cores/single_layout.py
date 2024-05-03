from tkinter import ttk


class SingleLayout:
    def __init__(self, root):
        ttk.Label(master=root, anchor="center", text="GuiUniAPP").grid(
            row=0, column=0, padx=10, pady=10, sticky="NESW"
        )

        self.application = ttk.Frame(master=root, width=850, height=400)

    def main(self):
        self.application.grid(row=1, column=0, padx=20, pady=20)

        return self
