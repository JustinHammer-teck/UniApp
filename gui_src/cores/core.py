import importlib.util

from cores.controller import Controller
from cores.view import View


class Core:
    current_view: View | None
    current_controller: Controller | None

    def __init__(self, parent):
        self.root = parent
        self.current_view = None
        self.current_controller = None
        self.is_auth = False

    def controller(self, controller: str, action: str = "main", **kwargs):
        try:
            module = self.__check_module_existent(
                f"controllers.{controller.lower()}_controller"
            )

            controller_class = getattr(module, f"{controller.capitalize()}Controller")

            if not self.__is_a_same_instance(controller_class):
                self.current_controller = controller_class(self)

            controller_action = getattr(self.current_controller, action)

            if action == "main" and self.current_controller:
                self.current_controller.set_view(self.view(view=controller.lower()))
                return controller_action()

            return controller_action(**kwargs)

        except (ImportError, AttributeError) as e:
            print(
                f"Error loading or executing controller: {controller}/{action} with error {e}"
            )

    def view(self, view: str, partial="main"):
        try:
            module = self.__check_module_existent(f"views.{view.lower()}_view")
            view_class = getattr(module, f"{view.capitalize()}View")

            if not self.current_view:
                self.current_view = view_class(self)
            elif self.current_view and not isinstance(
                view_class, type(self.current_view)
            ):
                self.current_view.close()

                for widgets in self.root.winfo_children():
                    widgets.destroy()

                self.current_view = view_class(self)

            view_partial = getattr(self.current_view, partial)
            return view_partial()

        except (ImportError, AttributeError) as e:
            # Handle the error (module or class or method not found)
            print(f"Error loading view: {view}/{partial} with error {e}")

    def show_error_window(self):
        pass

    def __is_a_same_instance(self, controller_cls):
        return self.current_controller and isinstance(
            controller_cls, type(self.current_view)
        )

    def __check_module_existent(self, module):
        try:
            return importlib.import_module(module)
        except ModuleNotFoundError:
            print("module {module} not found")
            raise
