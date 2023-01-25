from tkinter import *
import time, threading
import tkinter.messagebox

class Game(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Demonstrating Keystroke Events")

        self.canvas = Canvas(self, width=600, height=600)
        self.canvas.pack()

        self.PlayerImage = PhotoImage(file='spaceship1.png')
        self.EnemyImage = PhotoImage(file='rock.png')
        self.canvas.create_image(80, 150, image=self.PlayerImage, anchor=NW, tags='player')
        self.canvas.move('player', -50, -50)

        self.canvas.create_image(100, 10, image=self.EnemyImage, anchor=NW, tags='enemy')
        self.canvas.create_image(10, 10, image=self.EnemyImage, anchor=NW, tags='enemy')

        self.master.bind("<KeyRelease>", self.move_Player)
        move_enemy(self.canvas)


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

def move_enemy(use_this_canvas):
    print(time.ctime())
    try:
        use_this_canvas.move('enemy', +2, 0)

        threading.Timer(1, move_enemy, [use_this_canvas]).start()
    except:
        print("Hej zapomniałeś zamknąć osobnego wątku. Spoko zrobiłem to za ciebie. Uzyłem try i except")


Game().mainloop()