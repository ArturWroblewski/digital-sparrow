from tkinter import *


class KeyDemo(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Demonstrating Keystroke Events")
        #self.master.geometry("350x200")

        self.canvas = Canvas(self, width=200, height=200)
        self.canvas.pack()

        self.PlayerImage = PhotoImage(file='spaceship1.png')

        self.canvas.create_image(80, 150, image=self.PlayerImage, anchor=NW, tags='player')
        self.canvas.move('player', -100, -100)

        self.master.bind("<KeyRelease>", self.move_Player)


    def move_Player(self, event):
        print(event.keysym)
        if event.keysym == "Up":
            self.canvas.move('player', 0, -10)
        elif event.keysym == "Down":
            self.canvas.move('player', 0, 10)
        elif event.keysym == "Left":
            self.canvas.move('player', -10, 0)
        elif event.keysym == "Right":
            self.canvas.move('player', 10, 0)


KeyDemo().mainloop()