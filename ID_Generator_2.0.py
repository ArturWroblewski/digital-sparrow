from tkinter import *
import socket
import random
root = Tk()

bitID_01 = 0
bitID_02 = 0
bitID_03 = 0
bitID_04 = 0



UDP_IP = "127.0.0.1"
UDP_PORT = 5005
text = "Hello, World!"
aUDP_counter = 0

def SendUDP(event):
    print("SEND UDP PACK")
    UDP_IP = entery_7.get()
    UDP_PORT = int(entery_8.get())
    text = outTextBox.get()
    MESSAGE = bytes(text, 'utf-8')

    print("UDP target IP:", UDP_IP)
    print("UDP target port:", UDP_PORT)
    print("message:", MESSAGE)
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    #sock.sendto(MESSAGE, (UDP_IP, UDP_PORT)) # Nie uzywane polecenie do testów

    data = bytearray([0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 40, 97, 98, 99, 100, 101])
    data.append(0x06)
    data.append(0xFF)
    xMax = int(entery_5.get());
    for x in range(xMax):
        data.append(random.randrange(255))

    sock.sendto(data, (UDP_IP, UDP_PORT))
    print("send bytes:", len(data))



def printName2(event):
    print("Start Generate ID")
    Slot = int(entery_1.get())

    Resolution = int(entery_2.get())
    ResolutionCode=0



    if Resolution<=16 and Resolution>8:
        ResolutionCode = 1

    if Resolution<=24 and Resolution>16:
        ResolutionCode = 2

    if Resolution<=32 and Resolution>24:
        ResolutionCode = 3
    if Resolution<=30 and Resolution>32:
        ResolutionCode = 4
    if Resolution <= 48 and Resolution > 40:
        ResolutionCode = 5
    if Resolution <= 56 and Resolution > 48:
        ResolutionCode = 6
    if Resolution<=64 and Resolution>56:
        ResolutionCode = 7

    AnalogCh = int(entery_3.get())
    DigitalCh = int(entery_4.get())
    DigitalChCode = int(DigitalCh/8)

    if (DigitalCh&0x07) > 0:
        DigitalChCode = DigitalChCode+1; #Jezeli jest mniej niż 8 kanałów dodaj 1 byte do transmisji z niepełną liczbą

    bitID_01 = (Slot<<2) + (AnalogEnable.get()<<1) +DigitalEnable.get()
    bitID_02 = (ResolutionCode << 3) + (AnalogInOut.get() << 6) + (DigitalInOut.get() << 7)
    bitID_03 = AnalogCh # 8bit + 3 bit
    bitID_04 = DigitalChCode

    #outTextBox.insert(END, Slot*Resolution*AnalogCh*DigitalCh)
    outTextBox.delete(0, END)
    outTextBox.insert(END, (bitID_01<<24) + (bitID_02<<16)+ (bitID_03<<8) + bitID_04)
    outHEXTextBox.delete(0, END)
    outHEXTextBox.insert(END,hex(int(outTextBox.get())))
    outBINTextBox.delete(0, END)
    outBINTextBox.insert(END,bin(int(outTextBox.get())))

root.title("Generate ID for UDP");
#byte 0
label_1 = Label(root, text="Slot (0-63)")
label_2 = Label(root, text="Analog Enable")
label_3 = Label(root, text="Digital Enable")
#byte 1
label_4 = Label(root, text="ExtendetFrame")
label_5 = Label(root, text="Reserved bit")
label_6 = Label(root, text="ADC Resolution 0-32 bit")
#byte 2 + 1
label_7 = Label(root, text="Number of Analog channels (0-2047):")
#byte 3
label_8 = Label(root, text="Number of Digital channels (0-2040):")

label_9 = Label(root, text="Length of digital outputs")
label_10 = Label(root, text="Counter")

label_11 = Label(root, text="IP Adress")
label_12 = Label(root, text="Port")
label_13 = Label(root, text="Message")

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

entery_5 = Entry(root)
entery_6 = Entry(root)

entery_7 = Entry(root)
entery_8 = Entry(root)
entery_9 = Entry(root)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)
label_3.grid(row=2, sticky=E)
label_4.grid(row=3, sticky=E)
label_5.grid(row=4, sticky=E)
label_6.grid(row=5, sticky=E)
label_7.grid(row=6, sticky=E)
label_8.grid(row=7, sticky=E)

label_9.grid(row=8, sticky=E)
label_10.grid(row=9, sticky=E)

label_11.grid(row=10, sticky=E)
label_12.grid(row=11, sticky=E)
label_13.grid(row=12, sticky=E)

entery_1.grid(row=0,column=1)
CheckAnalogEnable.grid(row=1,column=1)
CheckDigitalEnable.grid(row=2,column=1)
CheckAnalogInOut.grid(row=3,column=1)
CheckDigitalInOut.grid(row=4,column=1)
entery_2.grid(row=5,column=1)
entery_3.grid(row=6,column=1)
entery_4.grid(row=7,column=1)

entery_5.grid(row=8,column=1)
entery_6.grid(row=9,column=1)

entery_7.grid(row=10,column=1)
entery_8.grid(row=11,column=1)
entery_9.grid(row=12,column=1)

log_in_button = Button(root, text="Generate ID")
log_in_button.bind("<Button-3>", SendUDP)
log_in_button.bind("<Button-1>", printName2)
log_in_button.grid(columnspan=3)

#TextArea = Text()
entery_1.insert(END, '2')
entery_2.insert(END, '10')
entery_3.insert(END, '14')
entery_4.insert(END, '6')
CheckAnalogEnable.select();
CheckDigitalEnable.select();
entery_5.insert(END, '255')
entery_7.insert(END, '127.0.0.1')
entery_8.insert(END, '5005')

#TextArea.grid(columnspan=4)
outTextBox = Entry(root)
outTextBox.grid(columnspan=4)
outHEXTextBox = Entry(root)
outHEXTextBox.grid(columnspan=5)
outBINTextBox = Entry(root)
outBINTextBox.grid(columnspan=6)

send_button = Button(root, text="SEND UDP")
send_button.bind("<Button-1>", SendUDP)
send_button.grid(columnspan=3)

root.mainloop()