from tkinter import *

def hide_me(event):
    event.widget.pack_forget()

def add_me():
    btn3=Button(root, text="Click")
    btn3.bind('<Button-1>', hide_me)
    btn3.pack()
    btn2.pack()

root = Tk()

btn_show=Button(root, text="Show")
btn_show.bind(add_me)
btn_show.pack()
btn=Button(root, text="Click")
btn.bind('<Button-1>', hide_me)
btn.pack()
btn2=Button(root, text="Click too")
btn2.bind('<Button-1>', hide_me)
btn2.pack()
root.mainloop()