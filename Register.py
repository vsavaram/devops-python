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

    def execute(self):
        # Register user information
        username = input("Username:")
        user = self.fileHandler.get_row(username)
        if user is not None:
            print("User already exists.")
            return False

        password = input("Password:")
        full_name = input("Fullname:")
        phone_number = input("Phone number:")
        while not self.is_number(phone_number):
            print("Only numbers allowed")
            phone_number = input("Phone number:")

        self.fileHandler.add_row(username, password, full_name, phone_number)
        self.fileHandler.write_table()

        # Check if user exists and print data
        user = self.fileHandler.get_row(username)
        if user is not None:
            if username == user[0] and password == user[1]:
                print("User %s registered successfully" % user[0])
                print("Full name: %s" % user[2])
                print("Phone number: %s" % user[3])
                return True

        print("Something went wrong with registration!!!")
        return False
