import tkinter as tk


class SingleLayout:
    def __init__(self, root):
        self.label = tk.Label(master=root, anchor="center", text="GuiUniAPP")
        self.application = tk.Frame(master=root, width=650, height=400)

    def main(self):
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="NESW")
        self.application.grid(row=1, column=0, padx=20, pady=20)

        return self

    def close(self):
        self.label.destroy()
        self.application.destroy()
