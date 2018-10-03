
from FileReader import FileReader

# Parse the user database from file
fileReader = FileReader()
fileReader.parse(".\\users.txt")

# Fetch username and password from user
username = input("Username:")
password = input("Password:")

# Check if user exists and print data
user = fileReader.get_row(username)
if user is not None:
    if username == user[0] and password == user[1]:
        print("Logged in successfully")
        print("Full name: %s" %user[2])
        print("Phone number: %s" % user[3])
        exit(0)
print("Wrong username or password!!!")