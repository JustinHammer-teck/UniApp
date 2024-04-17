import importlib.util

from config import APP_PATH


class Core:
    def __init__(self, parent):
        self.root = parent

    def controller(self, controller: str, action="main"):

        try:
            controller_path = (
                f"{APP_PATH}/controllers/{controller.lower()}_controller.py"
            )

            module = importlib.import_module(
                f"controllers.{controller.lower()}_controller"
            )

            controller_class = getattr(module, f"{controller.capitalize()}Controller")

            controller_instance = controller_class()

            controller_action = getattr(controller_instance, action)

            controller_action().main()

        except (ImportError, AttributeError) as e:
            # Handle the error (module or class or method not found)
            print(f"Error loading or executing controller: {e}")
            return None
