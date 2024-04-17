import abc

from cores.default_layout import DefaultLayout


class View(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def main(self):
        return

    @abc.abstractmethod
    def close(self):
        return
