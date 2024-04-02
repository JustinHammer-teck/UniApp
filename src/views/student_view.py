from getpass import getpass


class StudentView:

    def login(self, *msg):

        if msg:
            print(msg)

        username = input("your username: ")
        password = getpass("your password: ")

        return (username, password)
