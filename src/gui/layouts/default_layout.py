import tkinter as tk


class DefaultLayout:
    def __init__(self, root):
        self.label = tk.Label(master=root, anchor="center", text="GUIUNIAPP")
        self.application = tk.Frame(
            master=root, width=650 // 4, height=400, bg="#135D66"
        )
        self.menu = tk.Frame(master=root, width=650 // 8, height=400)

    def main(self):
        self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="NESW")
        self.menu.grid(row=1, column=0, padx=10, pady=5)
        self.application.grid(row=1, column=1, padx=10, pady=5)
        return self

    def close(self):
        self.label.destroy()
        self.menu.destroy()
        self.application.destroy()
