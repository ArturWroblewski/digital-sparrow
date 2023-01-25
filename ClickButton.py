from tkinter import *

root = Tk()
def printName(event):
    print("Kliknoleś przycisk LOGIN")
def printName2(event):
    print("Kliknoleś przycisk LOGIN lewym przyciskiem")
root.title("Log In")

label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entery_1 = Entry(root)
entery_2 = Entry(root)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)

entery_1.grid(row=0,column=1)
entery_2.grid(row=1,column=1)

c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)

log_in_button = Button(root, text="Login")
log_in_button.bind("<Button-3>", printName)
log_in_button.bind("<Button-1>", printName2)
log_in_button.grid(columnspan=3)

root.mainloop()