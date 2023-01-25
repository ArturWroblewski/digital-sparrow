from tkinter import *
import time
import threading
from threading import Thread

import RPi.GPIO as GPIO
import socket
root = Tk()
root.geometry("250x450")
# https://wiki.python.org/moin/UdpCommunication
# https://www.geeksforgeeks.org/how-to-use-images-as-backgrounds-in-tkinter/
# https://linuxhint.com/gpio-pinout-raspberry-pi/

# Data
# Data

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

var_GPIO_1 = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(),
              IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(),
              IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(),
              IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()]

BytesToSends = bytearray([0, 0, 0, 0, 0])
BitsToSendsAll = 0
permission_for_multithreading = True

# Funkcje
# Data



def calculate_crc_last_byte():
    print("Read I/O")

    i = 0
    for int_var in var_GPIO_1:
        BitsToSendsAll = int_var.get() << i | BitsToSendsAll
        i += 1
    print(BitsToSendsAll.to_bytes(5, byteorder='big'))


def read_check_box_value():


    BitsToSends0 = var_GPIO_1[0].get() << 0 | var_GPIO_1[1].get() << 1 | var_GPIO_1[2].get() << 2 | var_GPIO_1[3].get() << 3 | var_GPIO_1[4].get() << 4 | var_GPIO_1[5].get() << 5 | var_GPIO_1[6].get() << 6 | var_GPIO_1[7].get()<<7
    BitsToSends1 = var_GPIO_1[8].get() << 0 | var_GPIO_1[9].get() << 1 | var_GPIO_1[10].get() << 2 | var_GPIO_1[11].get() << 3 | var_GPIO_1[12].get() << 4 | var_GPIO_1[13].get() << 5 | var_GPIO_1[14].get() << 6 | var_GPIO_1[15].get()<<7
    BitsToSends2 = var_GPIO_1[16].get() << 0 | var_GPIO_1[17].get() << 1 | var_GPIO_1[18].get() << 2 | var_GPIO_1[19].get() << 3 | var_GPIO_1[20].get() << 4 | var_GPIO_1[21].get() << 5 | var_GPIO_1[22].get() << 6 | var_GPIO_1[23].get()<<7
    BitsToSends3 = var_GPIO_1[24].get() << 0 | var_GPIO_1[25].get() << 1 | var_GPIO_1[26].get() << 2 | var_GPIO_1[27].get() << 3 | var_GPIO_1[28].get() << 4 | var_GPIO_1[29].get() << 5 | var_GPIO_1[30].get() << 6 | var_GPIO_1[31].get()<<7

    BytesToSends[0] = BitsToSends0
    BytesToSends[1] = BitsToSends1
    BytesToSends[2] = BitsToSends2
    BytesToSends[3] = BitsToSends3


def pritn_check_box_value():
    # Alternatywna wersja dodawania
    BitsToSendsAll = 0
    i=0
    for int_var in var_GPIO_1:
        BitsToSendsAll = int_var.get() << i | BitsToSendsAll
        i += 1
    print(BitsToSendsAll.to_bytes(5, byteorder='big'))





def calculate_crc_last_byte():
    Divider2 = False
    Divider3 = False
    Divider7 = False
    Divider11 = False
    Divider13 = False
    EndBit = True

    BitCount = BytesToSends[0].bit_count() + BytesToSends[1].bit_count() + BytesToSends[2].bit_count() + BytesToSends[3].bit_count()
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

    #print("bool: " , Divider2,Divider3,Divider7,EndBit)

    BitsToSends4 = int(False) << 0 | int(False) << 1 | int(Divider13) << 2 | int(Divider11) << 3 | int(Divider2) << 4 | int(Divider3) << 5 | int(Divider7) << 6 | int(EndBit) << 7
    BytesToSends[4] = BitsToSends4

    # print("Byte To Send: " , BytesToSends)
    print("Bits To Send: ", bin(int.from_bytes(BytesToSends, "big")))
    print("How many bits 1 : ", BitCount)


class thread(threading.Thread):
    def __init__(self, thread_name, thread_ID):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID

        # helper function to execute the threads

    def run(self):
        while permission_for_multithreading:
            print(str(self.thread_name) + " " + str(self.thread_ID))
            time.sleep(0.9)


def pritn_check_box_value2():
    # Alternatywna wersja dodawania
    BitsToSendsAll = 0
    i=0
    for int_var in var_GPIO_1:
        BitsToSendsAll = int_var.get() << i | BitsToSendsAll
        i += 1
        print(BitsToSendsAll.to_bytes(5, byteorder='big'))





def start_new_threads(event):
    print("Start new threads")
    global permission_for_multithreading
    permission_for_multithreading = True
    global thread1
    thread1 = thread("GFG", 1000)
    global thread2
    thread2 = thread("GeeksforGeeks", 2000);
    if not thread1.is_alive():
        thread1.start()
    if not thread2.is_alive():
        thread2.start()


def stop_new_threads(event):
    #print("Stop all threads", permission_for_multithreading)
    global permission_for_multithreading
    permission_for_multithreading = False
    thread1.join()
    thread2.join()


def print_text_by_right_mouse_click(event):
    print("Kliknoleś przycisk LOGIN prawym przyciskiem myszy")




def send_single_udp_frame_by_click(event):
    read_check_box_value()
    calculate_crc_last_byte()
    UDP_IP = entery_1.get()
    UDP_PORT = int(entery_3.get())
    # text = entery_4.get()
    # MESSAGE = bytes(text, 'utf-8')

    print ("UDP target IP:", UDP_IP)
    print ("UDP target port:", UDP_PORT)
    # print ("message:", MESSAGE)
    sock = socket.socket(socket.AF_INET, # Internet
    socket.SOCK_DGRAM) # UDP
    # sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

    # data = bytearray([0,0,0,0,1, 2, 3, 4, 5, 6,0,0,0,0,0,0,0,0,0,0,0,40,97,98,99,100,101])
    data = BytesToSends
    print("message:", data)
    sock.sendto(data, (UDP_IP, UDP_PORT))
    print("send bytes:", len(data))

    pritn_check_box_value()



# UI Create
# UI Files and Buttons

root.title("Send UDP")

label_1 = Label(root, text="IP Adress)")
label_1.grid(row=0, sticky=E)
label_7 = Label(root, text="UDP Port")
label_7.grid(row=1, sticky=E)
label_8 = Label(root, text="message")
label_8.grid(row=2, sticky=E)

entery_1 = Entry(root)
entery_1.grid(row=0, column=1)
entery_3 = Entry(root)
entery_3.grid(row=1, column=1)
entery_4 = Entry(root)
entery_4.grid(row=2, column=1)

send_button = Button(root, text="Send once")
send_button.bind("<Button-3>", print_text_by_right_mouse_click)
send_button.bind("<Button-1>", send_single_udp_frame_by_click)
send_button.grid(row=0,column=2)

stop_send_button = Button(root, text="Stop send")
stop_send_button.bind("<Button-1>", stop_new_threads)
stop_send_button.grid(row=2, column=2)
start_button = Button(root, text="Start send")
start_button.bind("<Button-1>", start_new_threads)
start_button.grid(row=1, column=2)

# UI Create
# UI Drawings

canvas = Canvas(root, width=150, height=310)
img = PhotoImage(file="Pin_list.png")
canvas.create_image(2, 2, anchor=NW, image=img)
canvas.place(x=80, y=83)

canvas2 = Canvas(root, width=230, height=45)
img2 = PhotoImage(file="Pin_legend.png")
canvas2.create_image(2, 2, anchor=NW, image=img2)
canvas2.place(x=15, y=400)

entery_1.insert(END, '127.0.0.1')
entery_3.insert(END, '5005')
entery_4.insert(END, 'UDP_message')

# UI Create
# UI CheckBox GPIO

# RPi I/0
# Right

c0 = Checkbutton( text='GPIO 2',variable=var_GPIO_1[0], onvalue=1, offvalue=0)
c0.place(x=0, y=105, height=15, width=80)
c1 = Checkbutton( text='GPIO 3',variable=var_GPIO_1[1], onvalue=1, offvalue=0)
c1.place(x=0, y=120, height=15, width=80)
c2 = Checkbutton( text='GPIO 4',variable=var_GPIO_1[2], onvalue=1, offvalue=0)
c2.place(x=0, y=135, height=15, width=80)

c3 = Checkbutton( text='GPIO 17',variable=var_GPIO_1[3], onvalue=1, offvalue=0)
c3.place(x=0, y=165, height=15, width=80)
c4 = Checkbutton( text='GPIO 27',variable=var_GPIO_1[4], onvalue=1, offvalue=0)
c4.place(x=0, y=180, height=15, width=80)
c5 = Checkbutton( text='GPIO 22',variable=var_GPIO_1[5], onvalue=1, offvalue=0)
c5.place(x=0, y=195, height=15, width=80)

c6 = Checkbutton( text='GPIO 10',variable=var_GPIO_1[6], onvalue=1, offvalue=0)
c6.place(x=0, y=225, height=15, width=80)
c7 = Checkbutton( text='GPIO 9',variable=var_GPIO_1[7], onvalue=1, offvalue=0)
c7.place(x=0, y=240, height=15, width=80)
c8 = Checkbutton( text='GPIO 11',variable=var_GPIO_1[8], onvalue=1, offvalue=0)
c8.place(x=0, y=255, height=15, width=80)

c9 = Checkbutton( text='GPIO 0',variable=var_GPIO_1[9], onvalue=1, offvalue=0)
c9.place(x=0, y=285, height=15, width=80)
c10 = Checkbutton( text='GPIO 5',variable=var_GPIO_1[10], onvalue=1, offvalue=0)
c10.place(x=0, y=300, height=15, width=80)
c11 = Checkbutton( text='GPIO 6',variable=var_GPIO_1[11], onvalue=1, offvalue=0)
c11.place(x=0, y=315, height=15, width=80)
c12 = Checkbutton( text='GPIO 13',variable=var_GPIO_1[12], onvalue=1, offvalue=0)
c12.place(x=0, y=330, height=15, width=80)
c13 = Checkbutton( text='GPIO 19',variable=var_GPIO_1[13], onvalue=1, offvalue=0)
c13.place(x=0, y=345, height=15, width=80)
c14 = Checkbutton( text='GPIO 26',variable=var_GPIO_1[14], onvalue=1, offvalue=0)
c14.place(x=0, y=360, height=15, width=80)

# RPi I/0
# Left

c15 = Checkbutton( text='GPIO 14',variable=var_GPIO_1[15], onvalue=1, offvalue=0)
c15.place(x=130, y=135, height=15, width=80)
c16 = Checkbutton( text='GPIO 15',variable=var_GPIO_1[16], onvalue=1, offvalue=0)
c16.place(x=130, y=150, height=15, width=80)
c17 = Checkbutton( text='GPIO 18',variable=var_GPIO_1[17], onvalue=1, offvalue=0)
c17.place(x=130, y=165, height=15, width=80)

c18 = Checkbutton( text='GPIO 23',variable=var_GPIO_1[18], onvalue=1, offvalue=0)
c18.place(x=130, y=195, height=15, width=80)
c19 = Checkbutton( text='GPIO 24',variable=var_GPIO_1[19], onvalue=1, offvalue=0)
c19.place(x=130, y=210, height=15, width=80)

c20 = Checkbutton( text='GPIO 25',variable=var_GPIO_1[20], onvalue=1, offvalue=0)
c20.place(x=130, y=240, height=15, width=80)
c21 = Checkbutton( text='GPIO 8',variable=var_GPIO_1[21], onvalue=1, offvalue=0)
c21.place(x=130, y=255, height=15, width=80)
c22 = Checkbutton( text='GPIO 7',variable=var_GPIO_1[22], onvalue=1, offvalue=0)
c22.place(x=130, y=270, height=15, width=80)
c23 = Checkbutton( text='GPIO 1',variable=var_GPIO_1[23], onvalue=1, offvalue=0)
c23.place(x=130, y=285, height=15, width=80)

c24 = Checkbutton( text='GPIO 12',variable=var_GPIO_1[24], onvalue=1, offvalue=0)
c24.place(x=130, y=315, height=15, width=80)

c25 = Checkbutton( text='GPIO 16',variable=var_GPIO_1[25], onvalue=1, offvalue=0)
c25.place(x=130, y=345, height=15, width=80)
c26 = Checkbutton( text='GPIO 20',variable=var_GPIO_1[26], onvalue=1, offvalue=0)
c26.place(x=130, y=360, height=15, width=80)
c27 = Checkbutton( text='GPIO 21',variable=var_GPIO_1[27], onvalue=1, offvalue=0)
c27.place(x=130, y=375, height=15, width=80)
# UI END

root.mainloop()