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
    print ("Start received on UDP port:", UDP_PORT)
    print ("Waiting for message")
    sock = socket.socket(socket.AF_INET, # Internet
    socket.SOCK_DGRAM) # UDP
    #sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    sock.bind((UDP_IP, UDP_PORT))
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        print ("received message:", data)
        print("received bytes:", len(data))


root.title("Retrive UDP");

label_1 = Label(root, text="IP Adress)")
label_2 = Label(root, text="UDP Port")
label_3 = Label(root, text="NA")

label_4 = Label(root, text="NA")
label_5 = Label(root, text="NA")
label_6 = Label(root, text="NA")
label_7 = Label(root, text="UDP Port")
label_8 = Label(root, text="message")

entery_1 = Entry(root)

AnalogEnable = IntVar()
DigitalEnable = IntVar()
AnalogInOut = IntVar()
DigitalInOut = IntVar()


CheckAnalogEnable = Checkbutton(root, text="",variable=AnalogEnable)
CheckDigitalEnable = Checkbutton(root, text="",variable=DigitalEnable)
CheckAnalogInOut = Checkbutton(root, text="",variable=AnalogInOut)
CheckDigitalInOut = Checkbutton(root, text="",variable=DigitalInOut)
entery_2 = Entry(root)
entery_3 = Entry(root)
entery_4 = Entry(root)


label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)
label_3.grid(row=2, sticky=E)
label_4.grid(row=3, sticky=E)
label_5.grid(row=4, sticky=E)
label_6.grid(row=5, sticky=E)
label_7.grid(row=6, sticky=E)
label_8.grid(row=7, sticky=E)

entery_1.grid(row=0,column=1)
CheckAnalogEnable.grid(row=1,column=1)
CheckDigitalEnable.grid(row=2,column=1)
CheckAnalogInOut.grid(row=3,column=1)
CheckDigitalInOut.grid(row=4,column=1)
entery_2.grid(row=5,column=1)
entery_3.grid(row=6,column=1)
entery_4.grid(row=7,column=1)

log_in_button = Button(root, text="Start receive")
log_in_button.bind("<Button-3>", printName)
log_in_button.bind("<Button-1>", printName2)
log_in_button.grid(columnspan=3)

#TextArea = Text()
entery_1.insert(END, '127.0.0.1')
entery_2.insert(END, '2')
entery_3.insert(END, '5005')
entery_4.insert(END, 'UDP_message')
CheckAnalogEnable.select();
CheckDigitalEnable.select();



#TextArea.grid(columnspan=4)
outTextBox = Entry(root)
outTextBox.grid(columnspan=4)
outHEXTextBox = Entry(root)
outHEXTextBox.grid(columnspan=5)
outBINTextBox = Entry(root)
outBINTextBox.grid(columnspan=6)

root.mainloop()