from json import loads
import os
from typing import List
from models.student import Student


class Database:
    db_path: str = "../../student.data"

    def read(self) -> List[Student]:
        studentList = List[Student]
        with open(self.db_path, "r") as file:
            for line in file:

                studentList.append(json.loads(line))

    def save_student(self):
        pass

    def delete_student(self):
        pass

    def __file_exit(self):
        if not os.path.exists(self.db_path):
            print(f"file with {self.db_path} does not exited")
