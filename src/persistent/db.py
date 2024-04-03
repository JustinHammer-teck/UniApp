import os
import pickle
from typing import List

from ..common.singleton import SingletonMeta
from ..models.student import Student


class Database(metaclass=SingletonMeta):
    DB_PATH: str = os.path.dirname(__file__) + "/students.data"
    context: List[Student]

    def __init__(self) -> None:
        self.context = []
        self.__load()

    def __load(self):
        self.read()

    def read(self) -> List[Student]:
        if self.__file_exited():
            with open(self.DB_PATH, "rb") as file:
                self.context = pickle.load(file)
        return self.context

    def save(self):
        try:
            with open(self.DB_PATH, "wb") as file:
                pickle.dump(self.context, file)
        except Exception as e:
            print(str(e))

    def __file_exited(self) -> bool:
        if not os.path.exists(self.DB_PATH):
            print(f"file with {self.DB_PATH} does not exited")
            return False
        return True
