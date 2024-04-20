from tkinter import ttk


class DefaultLayout:
    def __init__(self, root):
        self.applicaton = ttk.Frame(master=root)
        self.menu = ttk.Frame(master=root)

        self.menu_widget()
        self.application_widget()

    def menu_widget(self):
        self.menu.grid()

    def application_widget(self):
        pass

    def main(self):
        return self
