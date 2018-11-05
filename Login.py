class Login:
    def __init__(self, file_handler):
        self.fileHandler = file_handler

    def execute(self, username, password):
        result = ""
        # Check if user exists and print data
        user = self.fileHandler.get_row(username)
        if user is not None:
            if username == user[0] and password == user[1]:
                result += "Logged in successfully\n"
                result += "Full name: " + user[2] + "\n"
                result += "Phone number: " + user[3] + "\n"
                return result

        result += "Wrong username or password!!!\n"
        return result
