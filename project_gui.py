from tkinter import *
from FileHandler import FileHandler
from Login import Login
from Register import Register

# Parse the user database from file
fileHandler = FileHandler()
fileHandler.parse(".\\users.txt")


def login_command():
    login = Login(fileHandler)
    username = entry_username.get()
    password = entry_password.get()
    output = login.execute(username, password)
    lbl_status.config(text=output)


def register_command():
    register = Register(fileHandler)
    username = entry_username.get()
    password = entry_password.get()
    fullname = entry_fullname.get()
    email = entry_email.get()
    phone = entry_phone.get()
    output = register.execute(username, password, fullname, email, phone)
    lbl_status.config(text=output)


window = Tk()
window.title("Welcome to the world of python!!")
window.geometry("500x200")
window.configure(bg="Orange")

lr_frame = Frame(window)
lr_frame.grid(row=1, column=2, sticky=N)

details_frame = Frame(window, bg="Orange")
details_frame.grid(row=1, column=0)

status_frame = Frame(window)
status_frame.grid(row=1, column=1)

login_button = Button(lr_frame, text="Login", command=login_command)
login_button.grid(row=0, column=0)

register_button = Button(lr_frame, text="Register", command=register_command)
register_button.grid(row=0, column=1)

lbl_username = Label(details_frame, text="Username", bd=5, bg="Orange")
lbl_username.grid(row=0, sticky=W)
# label1.grid(sticky=W)

lbl_password = Label(details_frame, text="Password", bd=5, bg="Orange")
lbl_password.grid(row=1, sticky=W)

lbl_fullname = Label(details_frame, text="Full name", bd=5, bg="Orange")
lbl_fullname.grid(row=2, sticky=W)

lbl_email = Label(details_frame, text="Email", bd=5, bg="Orange")
lbl_email.grid(row=3, sticky=W)

lbl_phone = Label(details_frame, text="Phone number", bd=5, bg="Orange")
lbl_phone.grid(row=4, sticky=W)

lbl_status = Label(status_frame, text="", bd=10, bg="Orange", font=("Arial Bold", 10))
lbl_status.grid(sticky=S)

entry_username = Entry(details_frame, width=20)
entry_username.grid(row=0, column=1)
entry_username.focus()
entry_password = Entry(details_frame, width=20)
entry_password.grid(row=1, column=1)

entry_fullname = Entry(details_frame, width=20)
entry_fullname.grid(row=2, column=1)

entry_email = Entry(details_frame, width=20)
entry_email.grid(row=3, column=1)

entry_phone = Entry(details_frame, width=20)
entry_phone.grid(row=4, column=1)
#checkbutton = Checkbutton(window)
#checkbutton.grid(columnspan=2, sticky=W)

#img = PhotoImage(file="land")
#img.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W+E+N+S, padx=5, pady=5)

window.mainloop()