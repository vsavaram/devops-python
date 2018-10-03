class Login:
    def __init__(self, file_handler):
        self.fileHandler = file_handler

    def execute(self):
        # Fetch username and password from user
        username = input("Username:")
        password = input("Password:")

        # Check if user exists and print data
        user = self.fileHandler.get_row(username)
        if user is not None:
            if username == user[0] and password == user[1]:
                print("Logged in successfully")
                print("Full name: %s" % user[2])
                print("Phone number: %s" % user[3])
                return True
        print("Wrong username or password!!!")
        return False
