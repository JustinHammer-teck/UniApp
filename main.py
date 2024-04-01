class Sumthing:
    name: str
    age: int
    subjects: list[str]

    def __init__(self, name: str, age: int, subjects: list[str]) -> None:
        self.name = name
        self.age = age
        self.subjects = subjects


def main():

    myObj = Sumthing("Jason", 40, ["db", "architecture"])

    file = open("./student.data", "wb")

    file.write(myObj.encode())

    file.close()

    file = open("./student.data", "rb")

    result = file.read()
    print(result.decode("utf-8"))

    file.close()


if __name__ == "__main__":
    main()
