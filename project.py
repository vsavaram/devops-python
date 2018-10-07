from FileHandler import FileHandler
from Login import Login
from Register import Register

# Parse the user database from file
fileHandler = FileHandler()
fileHandler.parse(".\\users.txt")

prompt = input("Do you want to register a new user??(y/n)")
if prompt is not 'y':
    prompt = input("Do you want to login??(y/n)")
    if prompt is not 'y':
        print("Then get out of here!")
        exit(-1)
    else:
        login = Login(fileHandler)
        login.execute()
        exit(0)
else:
    register = Register(fileHandler)
    register.execute()

