class Database():
    db: str -> "./student.data"

    def read_data(self, arg):
        try:
            file = open(db, "rb")

        except Exception as e:
            raise e
        finally:
            file.close()
