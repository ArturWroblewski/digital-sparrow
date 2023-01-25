from tkinter import *

root = Tk()

bitID_01 = 0
bitID_02 = 0
bitID_03 = 0
bitID_04 = 0

def printName(event):
    print("Kliknoleś przycisk LOGIN")
def printName2(event):
    print("Start Generate ID")
    Slot = int(entery_1.get())

    Resolution = int(entery_2.get())
    ResolutionCode=0

    if Resolution<=8 and Resolution>0:
        ResolutionCode = 1

    if Resolution<=16 and Resolution>8:
        ResolutionCode = 2

    if Resolution<=24 and Resolution>16:
        ResolutionCode = 3

    if Resolution<=32 and Resolution>24:
        ResolutionCode = 4
    if Resolution<=64 and Resolution>32:
        ResolutionCode = 5
    if Resolution <= 128 and Resolution > 64:
        ResolutionCode = 6
    if Resolution <= 256 and Resolution > 128:
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

label_1 = Label(root, text="Slot (0-63)")
label_2 = Label(root, text="Analog Enable")
label_3 = Label(root, text="Digital Enable")

label_4 = Label(root, text="input/output Analog")
label_5 = Label(root, text="input/output Digital")
label_6 = Label(root, text="ADC Resolution 0-32 bit")
label_7 = Label(root, text="Number of Analog channels (0-2047):")
label_8 = Label(root, text="Number of Digital channels (0-2040):")

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

log_in_button = Button(root, text="Generate ID")
log_in_button.bind("<Button-3>", printName)
log_in_button.bind("<Button-1>", printName2)
log_in_button.grid(columnspan=3)

#TextArea = Text()
entery_1.insert(END, '2')
entery_2.insert(END, '2')
entery_3.insert(END, '14')
entery_4.insert(END, '6')
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