import os
import pickle
from typing import Any, List
from ..models.student import Student


class Database:
    DB_PATH: str = "../../student.data"

    def read(self) -> List[Student]:
        studentList: List[Student] = []
        if self.__file_exited():
            with open(self.DB_PATH, "rb") as file:
                for line in file:
                    studentList.append(pickle.loads(line))
        return studentList

    def write(self, obj: Any) -> int:
        return 0

    def __file_exited(self) -> bool:
        if not os.path.exists(self.DB_PATH):
            print(f"file with {self.DB_PATH} does not exited")
            return False
        return True
