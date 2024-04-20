import abc


class Controller(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def main(self):
        pass
