import abc

from gui.cores.view import View


class Controller(metaclass=abc.ABCMeta):
    view: View

    @abc.abstractmethod
    def main(self):
        pass

    def set_view(self, view):
        self.view = view
