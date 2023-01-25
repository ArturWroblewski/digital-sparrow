from distutils import command
from tkinter import *
from tkinter import ttk
# ** https://matplotlib.org/tutorials/colors/colors.html
def doNothing():
    print("I do nothing... it's no my fault")


root = Tk()
root.title("GUI base model sample")
root.minsize(600, 400)
root.maxsize(1920, 1080)

root.geometry('800x480')

# ***** MenuBar *****

#menu_Top = Menu(root)
menu_Top = Menu(root, background='#535353', foreground='white', activebackground='#004c99', activeforeground='white')
root.config(bg='#2A2C2B',menu=menu_Top)

# ***** Menu *****

#subMenu_File = Menu(menu_Top)
subMenu_File = Menu(menu_Top, tearoff=0, background='#535353',foreground='white', activebackground='#004c99', activeforeground='white')

menu_Top.add_cascade(label="File",menu=subMenu_File)
subMenu_File.add_command(label="Open File",command = doNothing)
subMenu_File.add_command(label="Close File",command = doNothing)
subMenu_File.add_separator()
subMenu_File.add_command(label="Exit",command = doNothing)

subMenu_Edit = Menu(menu_Top, tearoff=0, background='#535353',foreground='white', activebackground='#004c99', activeforeground='white')
menu_Top.add_cascade(label="Edit",menu=subMenu_Edit)
subMenu_Edit.add_command(label="Edit_now",command = doNothing)
subMenu_Edit.add_command(label="Edit_now",command = doNothing)

subMenu_View = Menu(menu_Top, tearoff=0, background='#535353',foreground='white', activebackground='#004c99', activeforeground='white')
menu_Top.add_cascade(label="View",menu=subMenu_View)
subMenu_View.add_command(label="Edit_now",command = doNothing)
subMenu_View.add_command(label="Edit_now",command = doNothing)

subMenu_Window = Menu(menu_Top, tearoff=0, background='#535353',foreground='white', activebackground='#004c99', activeforeground='white')
menu_Top.add_cascade(label="Window",menu=subMenu_Window)
subMenu_Window.add_command(label="Edit_now",command = doNothing)
subMenu_Window.add_command(label="Edit_now",command = doNothing)

subMenu_Help = Menu(menu_Top, tearoff=0, background='#535353',foreground='white', activebackground='#004c99', activeforeground='white')
menu_Top.add_cascade(label="Help",menu=subMenu_Help)
subMenu_Help.add_command(label="Edit_now",command = doNothing)
subMenu_Help.add_command(label="Edit_now",command = doNothing)


# ***** Toolbars *****
# ***** Top *****

toolbar_top = Frame(root, bg = "#535353")

photo=PhotoImage(file="Icon_1.png")
photo2=PhotoImage(file="Icon_2.png")

insertButton1= Button(toolbar_top, image=photo,width="28",height="28",anchor=NE,bd=0,bg="#535353",activebackground="#333333", command=doNothing)
insertButton1.pack(side=LEFT, padx=1, pady=0)
insertButton2= Button(toolbar_top, image=photo,anchor=NE,bd=0,bg="#535353",activebackground="#333333", command=doNothing)
insertButton2.pack(side=LEFT, padx=1, pady=0)



x1=Button(root)
x1.config(image=photo2,width="28",height="28",activebackground="#535353"
,bg="#535353", bd=0,command=doNothing)
x1.place(relx=1,x=5, y=-1, anchor=NE)
toolbar_top.pack(side=TOP, fill=X)

# ***** Center Frame Background *****#424242
Center_Frame = Frame(root, bg = "#282828")
Center_Frame.pack(side=TOP, fill=BOTH, expand=1, padx=0, pady=1)

# ***** Left Space Tollbar Standard *****
Left_Space = Frame(Center_Frame, bg = "#535353")
Left_Space.pack(side=LEFT, fill=Y, padx=0, pady=1)

# ***** Right Space Tollbar and WorkSpace ***** #424242
Right_Frame = Frame(Center_Frame, bg = "#282828")
Right_Frame.pack(side=TOP, fill=BOTH, expand=1, padx=0, pady=0)

Right_Space = Frame(Right_Frame, bg = "#535353")
Right_Space.pack(side=RIGHT, fill=Y, padx=0, pady=1)

WorkSpace = Frame(Right_Frame, bg = "#424242")
WorkSpace.pack(side=RIGHT, fill=BOTH, padx=2, pady=1,expand=1)

# ***** Insert Button to Left Tollbar and WorkSpace *****
insertButton3= Button(Left_Space, image=photo,width="36",height="36",bd=0,bg="#535353",activebackground="#333333", command=doNothing)
insertButton3.pack(side=TOP, padx=0, pady=1)

insertButton4= Button(Right_Space, image=photo,width="36",height="36",bd=0,bg="#535353",activebackground="#333333", command=doNothing)
insertButton4.pack(side=TOP, padx=0, pady=1)
# ****** anchor=NE,

# ***** Left *****



toolbar_Left = Frame(root, bg = "#535353")
insertButton3= Button(toolbar_top, image=photo,width="28",height="28",anchor=NE,bd=0,bg="#535353",activebackground="#333333", command=doNothing)
insertButton3.pack(side=TOP, padx=0, pady=1)
toolbar_Left.pack(side=LEFT, fill=Y)

mainloop()