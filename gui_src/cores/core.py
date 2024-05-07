import importlib.util

from cores.controller import Controller
from cores.view import View


class Core:
    current_view: View | None
    current_controller: Controller | None
    user: None

    def __init__(self, parent):
        self.root = parent
        self.current_view = None
        self.current_controller = None
        self.is_auth = False
        self.user = None

    def controller(self, controller_name: str, action: str = "main", **kwargs):
        try:
            controller_class = self.__try_get_module("controller", controller_name)

            if not self.__is_a_same_instance(controller_class):
                del self.current_controller
                self.current_controller = controller_class(self)

            controller_action = getattr(self.current_controller, action)

            if action == "main" and self.current_controller:
                self.current_controller.set_view(
                    self.view(view_name=controller_name.lower())
                )
                return controller_action()

            return controller_action(**kwargs)

        except (ImportError, AttributeError) as e:
            print(
                f"Error loading or executing controller: {controller_name}/{action} with error {e}"
            )

    def view(self, view_name: str, action="main", **kwargs):
        try:
            view_class = self.__try_get_module("view", view_name)

            if self.current_view:
                self.current_view.close()

                del self.current_view
            self.current_view = view_class(self)

            view_partial = getattr(self.current_view, action)
            self.root.update()
            view_partial()

        except (ImportError, AttributeError) as e:
            # Handle the error (module or class or method not found)
            print(f"Error loading view: {view_name}/{action} with error {e}")

    def logout(self):
        self.is_auth = False
        self.user = None

    def show_error_window(self):
        pass

    def __try_get_module(self, core: str, module_name: str):
        module = self.__check_module_existent(f"{core.lower()}s.{module_name.lower()}")
        return getattr(module, f"{module_name.capitalize()}{core.capitalize()}")

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
