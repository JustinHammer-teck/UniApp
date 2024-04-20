import importlib.util

from .default_layout import DefaultLayout


class Core:

    def __init__(self, parent):
        self.root = parent
        self.current_view = None

    def controller(self, controller: str, action="main"):
        try:
            module = importlib.import_module(
                f"controllers.{controller.lower()}_controller"
            )

            controller_class = getattr(module, f"{controller.capitalize()}Controller")
            controller_instance = controller_class()

            if action == "main":
                controller_instance.set_view(self.view(controller.lower()))

            controller_action = getattr(controller_instance, action)
            controller_action()

        except (ImportError, AttributeError) as e:
            # Handle the error (module or class or method not found)
            print(f"Error loading or executing controller: {e}")

    def view(self, view: str, partial="main"):
        try:
            if self.current_view:
                self.current_view.destroy()

            module = importlib.import_module(f"views.{view.lower()}_view")
            view_class = getattr(module, f"{view.capitalize()}View")
            self.current_view = view_class(DefaultLayout(self.root), self)
            view_partial = getattr(self.current_view, partial)
            view_partial()

        except (ImportError, AttributeError) as e:
            # Handle the error (module or class or method not found)
            print(f"Error loading view: {e}")
            raise e
