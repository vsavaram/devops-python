from tkinter import *
from FileHandler import FileHandler
from Login import Login


class LoginFrame:
    def __init__(self, file_handler, frame):
        self.fileHandler = file_handler

        self.details_frame = Frame(frame, bg="Orange")
        self.details_frame.grid(row=0, column=0)

        self.lbl_username = Label(self.details_frame, text="Username", bd=5, bg="Orange")
        self.lbl_username.grid(row=0, sticky=W)
        self.lbl_password = Label(self.details_frame, text="Password", bd=5, bg="Orange")
        self.lbl_password.grid(row=1, sticky=W)

        self.entry_username = Entry(self.details_frame, width=20)
        self.entry_username.grid(row=0, column=1)
        self.entry_username.focus()
        self.entry_password = Entry(self.details_frame, width=20)
        self.entry_password.grid(row=1, column=1)

        self.status_frame = Frame(frame)
        self.status_frame.grid(row=1, column=0)

        self.lbl_status = Label(self.status_frame, text="", bd=10, bg="Orange", font=("Arial Bold", 10))
        self.lbl_status.grid(sticky=S)

        self.login_frame = Frame(frame)
        self.login_frame.grid(row=2, sticky=N)
        login_button = Button(self.login_frame, text="Login", command=self.login_command)
        login_button.grid(row=0, column=0)

    def login_command(self):
        login = Login(self.fileHandler)
        output = login.execute(
            self.entry_username.get(),
            self.entry_password.get())
        self.lbl_status.config(text=output)

    def show_frame(self):
        self.login_frame.grid()
        self.details_frame.grid()
        self.status_frame.grid()

    def hide_frame(self):
        self.login_frame.grid_remove()
        self.details_frame.grid_remove()
        self.status_frame.grid_remove()
