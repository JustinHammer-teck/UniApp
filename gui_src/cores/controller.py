import abc
import importlib
import tkinter as tk

from cores.default_layout import DefaultLayout


class Controller(metaclass=abc.ABCMeta):
    root: tk.Tk

    @abc.abstractmethod
    def main(self):
        pass

    def view(
        self,
        view: str,
    ):

        try:
            module = importlib.import_module(f"views.{view.lower()}_view")

            view_class = getattr(module, f"{view.capitalize()}View")

            view_instance = view_class(DefaultLayout(self.root))

            return view_instance

        except (ImportError, AttributeError) as e:
            # Handle the error (module or class or method not found)
            print(f"Error loading view: {e}")
            raise e
