from tkinter import *

import socket
root = Tk()
# https://wiki.python.org/moin/UdpCommunication

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
text = "Hello, World!"


def printName(event):
    print("Kliknoleś przycisk LOGIN")
def printName2(event):
    UDP_IP = entery_1.get()
    UDP_PORT = int(entery_3.get())
    text = entery_4.get()
    MESSAGE = bytes(text, 'utf-8')

    print ("UDP target IP:", UDP_IP)
    print ("UDP target port:", UDP_PORT)
    print ("message:", MESSAGE)
    sock = socket.socket(socket.AF_INET, # Internet
    socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

    data = bytearray([0,0,0,0,1, 2, 3, 4, 5, 6,0,0,0,0,0,0,0,0,0,0,0,40,97,98,99,100,101])
    print("message:", data)
    sock.sendto(data, (UDP_IP, UDP_PORT))
    print("send bytes:", len(data))

root.title("Send UDP");

label_1 = Label(root, text="IP Adress)")
label_2 = Label(root, text="UDP Port")

label_7 = Label(root, text="UDP Port")
label_8 = Label(root, text="message")

entery_1 = Entry(root)



entery_3 = Entry(root)
entery_4 = Entry(root)


label_1.grid(row=0, sticky=E)


label_7.grid(row=6, sticky=E)
label_8.grid(row=7, sticky=E)

entery_1.grid(row=0,column=1)


entery_3.grid(row=6,column=1)
entery_4.grid(row=7,column=1)

log_in_button = Button(root, text="Send")
log_in_button.bind("<Button-3>", printName)
log_in_button.bind("<Button-1>", printName2)
log_in_button.grid(columnspan=3)

#TextArea = Text()
entery_1.insert(END, '127.0.0.1')

entery_3.insert(END, '5005')
entery_4.insert(END, 'UDP_message')




#TextArea.grid(columnspan=4)
outTextBox = Entry(root)
outTextBox.grid(columnspan=4)


root.mainloop()