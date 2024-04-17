from tkinter import ttk


class DefaultLayout(ttk.Frame):
    def __init__(self, root):

        super().__init__(master=root)

        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")

        ttk.Label(self, text="Hola").grid(row=0, column=0)
        ttk.Button(self, text="Hola").grid(row=0, column=1)

        self.pack()
