import pickle
from typing import List


class Sumthing:
    name: str
    id: int
    mores: List[str]

    def __init__(self, name, id, mores) -> None:
        self.name, self.id, self.mores = name, id, mores


def main():

    file = open("./students.data", "wb")
    sumthing = Sumthing("HI", 123, ["Sumethin", "is", "awesome"])
    pickle.dump(sumthing, file)

    file.close()

    try:
        with open("./students.data", "rb") as file:
            for line in file:
                student: Sumthing
                student = pickle.loads(line)
                print(student)

        file.close()
    except Exception as e:
        print(str(e))

    print("Hello World")


if __name__ == "__main__":
    main()
