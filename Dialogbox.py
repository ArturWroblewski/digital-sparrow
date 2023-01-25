from tkinter import *
from tkinter import filedialog
import xml.dom.minidom
import xml.etree.ElementTree
import tkinter.messagebox


root = Tk()
def printName(event):
    print("Kliknoleś przycisk LOGIN PRAWY")
    tkinter.messagebox.showinfo('Klik prawym przyciskiem', 'Monkeys can Live')

    anserw = tkinter.messagebox.askquestion('Pytanie 1','lubisz jesc?')

    if anserw == 'yes':
        print('Odpoowiedział tak hehe')


def printName2(event):
    print("Kliknoleś przycisk LOGIN lewym przyciskiem")

def printName3(event):
    root2 = Tk()
    root2.withdraw()

    file_path = filedialog.askopenfilename()


    #e = xml.etree.ElementTree.parse('thefile.xml').getroot()
    try:
        e = xml.etree.ElementTree.parse(file_path).getroot()
        for atype in e.findall('type'):
            print(atype.get('rozklad'))
        # dane
        doc = xml.dom.minidom.parse(file_path)
        print(doc.nodeName)
        print(doc.firstChild.tagName)
        #ZnalezionyElement = doc.
        #print(ZnalezionyElement)
    except Exception as Err:
        print("Błąd")
        print(Err)

def Menu(event):
    print("Teraz pownienem rozwinąć MENU")

root.title("Log In")
root.bind("<Button-3>", Menu)
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
log_in_button.bind("<Button-2>", printName3)
log_in_button.grid(columnspan=3)
root.mainloop()