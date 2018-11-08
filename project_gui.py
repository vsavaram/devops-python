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
mainWindow.title("Python!!")
mainWindow.geometry("250x300")
mainWindow.configure(bg="Orange")

topFrame = Frame(mainWindow, bg="Orange")
topFrame.grid(row=0, column=0, sticky=W)

newUserButton = Button(topFrame, text="New user", command=new_user_cmd)
newUserButton.grid(row=0, column=0, sticky=W)
getUserInfoButton = Button(topFrame, text="Get user information", command=user_info_cmd)
getUserInfoButton.grid(row=0, column=1, sticky=W)

mainFrame = Frame(mainWindow, bg="Orange")
mainFrame.grid(row=1, column=0, sticky=W)

loginFrame = LoginFrame(fileHandler, mainFrame)
registerFrame = RegisterFrame(fileHandler, mainFrame)

loginFrame.hide_frame()
registerFrame.hide_frame()

mainWindow.mainloop()
