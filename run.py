#from tkinter.ttk import Frame, Style
from tkinter.ttk import *
from tkinter import BOTH, Tk

class Okno(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent
        self.inicjalizuj()
    def inicjalizuj(self):
        self.parent.title("PyCharm window")
        self.styl=Style()
        self.styl.theme_use("default")

        self.pack(fill=BOTH, expand=1)
def main():
    gui=Tk()
    theLabel = Label(gui, text="Rozwiniecie: ");
    theLabel.pack()
    gui.geometry("1280x720")
    app=Okno(gui)
    gui.mainloop()

if __name__ == '__main__':
    main()


print("startprogram")

x = 92332
print("Wpisz jakis tekst w konsole: ")
#y = input()
print(x)
#print(type(y))


