from tkinter import *
from FileHandler import FileHandler
from LoginFrame import LoginFrame
from RegisterFrame import RegisterFrame

# Parse the user database from file
fileHandler = FileHandler()
fileHandler.parse(".\\users.txt")


def new_user_cmd():
    loginFrame.hide_frame()
    registerFrame.show_frame()


def user_info_cmd():
    registerFrame.hide_frame()
    loginFrame.show_frame()
    newUserButton.grid()


mainWindow = Tk()
mainWindow.title("Welcome to the world of python!!")
mainWindow.geometry("500x200")
mainWindow.configure(bg="Orange")

topFrame = Frame(mainWindow)
topFrame.grid(row=0, sticky=N)

newUserButton = Button(topFrame, text="New user", command=new_user_cmd)
newUserButton.grid(row=0, column=0)
getUserInfoButton = Button(topFrame, text="Get user information", command=user_info_cmd)
getUserInfoButton.grid(row=0, column=1)

mainFrame = Frame(mainWindow)
mainFrame.grid(row=1, sticky=N)

loginFrame = LoginFrame(fileHandler, mainFrame)
registerFrame = RegisterFrame(fileHandler, mainFrame)

loginFrame.hide_frame()
registerFrame.hide_frame()

mainWindow.mainloop()
