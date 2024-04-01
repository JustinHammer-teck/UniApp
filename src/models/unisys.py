from models.admin import Admin
from models.student import Student


class UniSystem(object):

    db: str = "../../students.data"

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(UniSystem, cls).__new__(cls)
        return cls.instance
