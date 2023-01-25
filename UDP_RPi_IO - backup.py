from tkinter import *
import RPi.GPIO as GPIO
import socket
root = Tk()
root.geometry("250x400")
# https://wiki.python.org/moin/UdpCommunication
# https://www.geeksforgeeks.org/how-to-use-images-as-backgrounds-in-tkinter/
# https://linuxhint.com/gpio-pinout-raspberry-pi/
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
text = "Hello, World!"

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(25, GPIO.IN)
#if GPIO.input(25): # if port 25 == 1
#            print ("Port 25 is 1/HIGH/True - LED ON")
#http://razzpisampler.oreilly.com/ch07.html
#GPIO.setmode(GPIO.BCM)
#for x in range(0,27):
#    GPIO.setup(x, GPIO.IN,pull_up_down=GPIO.PUD_UP)

#Pinout Order
#2,3,4,17,27,22,10,9
#11,0,5,6,13,19,26,14
#15,18,23,24,25,8,7,1
#12,16,20,21

var_GPIO_1 = [IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),
              IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),
              IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),
              IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),]

print((42).bit_length())
print((True).bit_length())

bool = True
my_integer = int(bool)
my_integer2 = int(bool)<<7
print(my_integer)
print(type(my_integer))
print(my_integer2.bit_length())

print("Test: ")

BitsToSends0 = var_GPIO_1[0].get()<<0 | var_GPIO_1[1].get()<<1 | var_GPIO_1[2].get()<<2 | var_GPIO_1[3].get()<<3 | var_GPIO_1[4].get()<<4 | var_GPIO_1[5].get() | var_GPIO_1[6].get() | var_GPIO_1[7].get()<<7
BitsToSends1 = int(bool)<<0 | int(bool)<<1 | int(bool)<<2 | int(bool)<<3 | int(bool)<<4 | int(bool)<<5 | int(bool)<<6 | int(bool)<<7
BitsToSends2 = int(bool)<<0 | int(bool)<<1 | int(bool)<<2 | int(bool)<<3 | int(bool)<<4 | int(bool)<<5 | int(bool)<<6 | int(bool)<<7
BitsToSends3 = int(bool)<<0 | int(bool)<<1 | int(bool)<<2 | int(bool)<<3 | int(False)<<4 | int(False)<<5 | int(False)<<6 | int(False)<<7

BitsToSendsAll = 0
def ReadCheckboks():
    BitsToSendsAll = 0
    i=0
    for int_var in var_GPIO_1:
        BitsToSendsAll = int_var.get()<<i | BitsToSendsAll
        i+=1
    print(BitsToSendsAll.to_bytes(4, byteorder='big'))

print(BitsToSends0.bit_length())
(255).to_bytes(2, byteorder='big')
print(BitsToSends0.to_bytes(1, byteorder='big'))
print(type(BitsToSends0.to_bytes(1, byteorder='big')))

BytesToSends = bytearray([0,0,0,0,0])
BytesToSends[0] = BitsToSends0
BytesToSends[1] = BitsToSends1
BytesToSends[2] = BitsToSends2
BytesToSends[3] = BitsToSends3

Divider2 = False
Divider3 = False
Divider7 = False
Divider11 = False
Divider13 = False
EndBit = True

BitCount = BitsToSends0.bit_count() + BitsToSends1.bit_count() + BitsToSends2.bit_count() + BitsToSends3.bit_count()
if(BitCount%2>0):
    Divider2 = True
if(BitCount%3>0):
    Divider3 = True
if(BitCount%7>0):
    Divider7 = True
if(BitCount%11>0):
    Divider11 = True
if(BitCount%13>0):
    Divider13 = True

print("bool: " , Divider2,Divider3,Divider7,EndBit)

BitsToSends4 = int(False)<<0 | int(False)<<1 | int(Divider13)<<2 | int(Divider11)<<3 | int(Divider2)<<4 | int(Divider3)<<5 | int(Divider7)<<6 | int(EndBit)<<7
BytesToSends[4] = BitsToSends4

print("Byte To Send: " , BytesToSends)
print("Bits To Send: " , bin(int.from_bytes(BytesToSends, "big")))
print("Bit 1 : " , BitCount)

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
    ReadCheckboks()

root.title("Send UDP");

label_1 = Label(root, text="IP Adress)")
label_2 = Label(root, text="UDP Port")

label_7 = Label(root, text="UDP Port")
label_8 = Label(root, text="message")

entery_1 = Entry(root)



entery_3 = Entry(root)
entery_4 = Entry(root)


canvas = Canvas(root, width = 150, height = 305)
img = PhotoImage(file="Pin_list.png")
canvas.create_image(00,00, anchor=NW, image=img)

label_1.grid(row=0, sticky=E)


label_7.grid(row=6, sticky=E)
label_8.grid(row=7, sticky=E)

entery_1.grid(row=0,column=1)


entery_3.grid(row=6,column=1)
entery_4.grid(row=7,column=1)
#canvas.grid(row=8,column=1)
#canvas.grid(row=8,column=1, rowspan=19)
canvas.place(x=80, y=90)
log_in_button = Button(root, text="Send")
log_in_button.bind("<Button-3>", printName)
log_in_button.bind("<Button-1>", printName2)
#log_in_button.grid(columnspan=3)
#img.grid(row=0, column=0, rowspan=6, padx=5, pady=5)
log_in_button.grid(row=7,column=2)

stop_send_button = Button(root, text="Stop")
stop_send_button.grid(row=8,column=2)
#TextArea = Text()
entery_1.insert(END, '127.0.0.1')

entery_3.insert(END, '5005')
entery_4.insert(END, 'UDP_message')


var_GPIO_2 = IntVar()

c0 = Checkbutton( text='GPIO 0',variable=var_GPIO_1[0], onvalue=1, offvalue=0)
#c0.grid(row=9,column=0)
c0.place(x=0, y=90, height=15, width=80)
c1 = Checkbutton( text='GPIO 1',variable=var_GPIO_1[1], onvalue=1, offvalue=0)
#c1.grid(row=10,column=0)
c1.place(x=0, y=105, height=15, width=80)

c2 = Checkbutton( text='GPIO 2',variable=var_GPIO_1[2], onvalue=1, offvalue=0)
#c2.grid(row=11,column=0)
c2.place(x=0, y=120, height=15, width=80)
c3 = Checkbutton( text='GPIO 3',variable=var_GPIO_1[3], onvalue=1, offvalue=0)
c3.place(x=0, y=135, height=15, width=80)
c4 = Checkbutton( text='GPIO 4',variable=var_GPIO_1[4], onvalue=1, offvalue=0)
c4.place(x=0, y=150, height=15, width=80)
c5 = Checkbutton( text='GPIO 4',variable=var_GPIO_1[5], onvalue=1, offvalue=0)
c5.place(x=0, y=165, height=15, width=80)
c6 = Checkbutton( text='GPIO 4',variable=var_GPIO_1[6], onvalue=1, offvalue=0)
c6.place(x=0, y=180, height=15, width=80)
#TextArea.grid(columnspan=4)
outTextBox = Entry(root)
outTextBox.grid(row=8,column=1)


root.mainloop()