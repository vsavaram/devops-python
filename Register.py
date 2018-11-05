class Register:
    def __init__(self, file_handler):
        self.fileHandler = file_handler

    @staticmethod
    def is_number(input_string):
        try:
            float(input_string)
            return True
        except ValueError:
            return False

    def execute(self, username, password, full_name, email, phone_number):
        # Register user information
        user = self.fileHandler.get_row(username)
        if user is not None:
            return "User already exists.\n"

        while not self.is_number(phone_number):
            return "Only numbers allowed\n"

        self.fileHandler.add_row(username, password, full_name, phone_number)
        self.fileHandler.write_table()

        # Check if user exists and print data
        user = self.fileHandler.get_row(username)
        if user is not None:
            if username == user[0] and password == user[1]:
                results = "User " + user[0] + " registered successfully\n"
                results += "Full name: " + user[2] + "\n"
                results += "Phone number: " + user[3] + "\n"
                return results

        return "Something went wrong with registration!!!"
