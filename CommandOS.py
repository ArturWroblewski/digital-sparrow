from tkinter import *
import subprocess

root = Tk()
root.title("Okno wysylające ping")

def printName(event):
    print("Kliknoleś przycisk prawym przyciskiem myszy")
    TextArea.delete('1.0', END)
    print("Wyczyszczenie")
def ButtonEventPing(event):

    print("Kliknoleś przycisk LOGIN lewym przyciskiem")
    #stdoutdata = subprocess.call(['ping', '10.1.0.31'])
    ipAddr = entery_1.get()
    process = subprocess.Popen(['ping', ipAddr], stdout=subprocess.PIPE)
    # print("2A stdoutdata: " + str(stdoutdata))
    stdout = process.communicate()[0]
    print('STDOUT:{}'.format(stdout))
    TextArea.insert(1.0, 'STDOUT:{}'.format(stdout))


label_1 = Label(root, text="IP addr:")
label_2 = Label(root, text="Port:")
entery_1 = Entry(root)
entery_1.insert(END, '10.1.0.31')
entery_2 = Entry(root)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)

entery_1.grid(row=0,column=1)
entery_2.grid(row=1,column=1)

TextArea = Text()

TextArea.grid(columnspan=4)

c = Checkbutton(root, text="Dodatkowy element nie uzywany w tej aplikacji")
c.grid(columnspan=2)

log_in_button = Button(root, text="Ping")
log_in_button.bind("<Button-3>", printName)
log_in_button.bind("<Button-1>", ButtonEventPing)
log_in_button.grid(columnspan=3)
root.mainloop()