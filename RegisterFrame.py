from tkinter import *
from FileHandler import FileHandler
from Register import Register


class RegisterFrame:
    def __init__(self, file_handler, frame):
        self.fileHandler = file_handler

        self.details_frame = Frame(frame, bg="Orange")
        self.details_frame.grid(row=0, sticky=W)

        self.lbl_username = Label(self.details_frame, text="Username", bd=5, bg="Orange")
        self.lbl_username.grid(row=0, sticky=W)
        self.lbl_password = Label(self.details_frame, text="Password", bd=5, bg="Orange")
        self.lbl_password.grid(row=1, sticky=W)
        self.lbl_fullname = Label(self.details_frame, text="Full name", bd=5, bg="Orange")
        self.lbl_fullname.grid(row=2, sticky=W)
        self.lbl_email = Label(self.details_frame, text="Email", bd=5, bg="Orange")
        self.lbl_email.grid(row=3, sticky=W)
        self.lbl_phone = Label(self.details_frame, text="Phone", bd=5, bg="Orange")
        self.lbl_phone.grid(row=4, sticky=W)

        self.entry_username = Entry(self.details_frame, width=20)
        self.entry_username.grid(row=0, column=1)
        self.entry_username.focus()
        self.entry_password = Entry(self.details_frame, width=20)
        self.entry_password.grid(row=1, column=1)
        self.entry_fullname = Entry(self.details_frame, width=20)
        self.entry_fullname.grid(row=2, column=1)
        self.entry_email = Entry(self.details_frame, width=20)
        self.entry_email.grid(row=3, column=1)
        self.entry_phone = Entry(self.details_frame, width=20)
        self.entry_phone.grid(row=4, column=1)

        self.status_frame = Frame(frame, bg="Orange")
        self.status_frame.grid(row=1, sticky=W)

        self.lbl_status = Label(self.status_frame, text="", bg="Orange", bd=5, font=("Arial Bold", 10))
        self.lbl_status.grid()

        self.register_frame = Frame(frame, bg="Orange")
        self.register_frame.grid(row=2, column=0, sticky=E)
        self.register_button = Button(self.register_frame, text="Register", command=self.run_register_cmd)
        self.register_button.grid(row=0, column=0, sticky=E)

    def run_register_cmd(self):
        register = Register(self.fileHandler)
        output = register.execute(
            self.entry_username.get(),
            self.entry_password.get(),
            self.entry_fullname.get(),
            self.entry_email.get(),
            self.entry_phone.get())
        self.lbl_status.config(text=output)

    def show_frame(self):
        self.register_frame.grid()
        self.details_frame.grid()
        self.status_frame.grid()

    def hide_frame(self):
        self.register_frame.grid_remove()
        self.details_frame.grid_remove()
        self.status_frame.grid_remove()
