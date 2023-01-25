from tkinter import *



root = Tk()

canvas = Canvas(root, width=200, height=200)
canvas.pack()

blackLine = canvas.create_line(0,0,200,50)
redLine = canvas.create_line(0,100,200,50,fill ="red")
greenBox = canvas.create_rectangle(25,25,75,75, fill='green')

gif1 = PhotoImage(file='spaceship1.png')

canvas.create_image(80, 150, image=gif1, anchor=NW, tags='player')
canvas.move('player', -100, -100)

#canvas.coords(gif1,10,10)
#canvas.delete(redLine)
#canvas.delete(ALL)

root.mainloop()