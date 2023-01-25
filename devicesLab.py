from tkinter import *
import random
import string
import devices
import slot
import socket
import array

root = Tk()



PackOfDevices = devices.Devices()

PackOfDevices.shearchDevicesTets()


print('Dostępnych uządzeń' , PackOfDevices.availableDevices.__len__())

PackOfDevices.printDevices()
PackOfDevices.availableDevices.__getitem__(2).availableSlots.append(slot.Slot(4))
PackOfDevices.availableDevices.__getitem__(2).availableSlots.append(slot.Slot(5))
PackOfDevices.availableDevices.__getitem__(1).availableSlots.append(slot.Slot(4))
PackOfDevices.availableDevices.__getitem__(1).availableSlots.append(slot.Slot(4))

for no in PackOfDevices.availableDevices:

    print('Urządzeńie SN:', no.serialNumber, 'IP:', no.ip,' Slotów:',no.availableSlots.__len__())
    no.printAvailbleSlots()
    print('Urządzeńie SN:', no.serialNumber, 'IP:', no.ip, ' Slotów:', len(no.availableSlots))


availableSlots = list()
for i in range(random.randrange(63)):
    availableSlots.append(slot.Slot(random.randrange(63)))
print('Urządzeńie SN:', ' Slotów:', availableSlots.__len__())
for no in availableSlots:
    print('Numery Slotów:', no.SlotNo)

PackOfDevices.printAvailbleDevices()

for liczba in range(0,10):
    i=liczba;
    if sys.getsizeof(i)==36:
        print('dla',i ,'Ciag znaków zajmuje - bytes',sys.getsizeof(i))



x ="a"
print ('ilosci znaków w ciagu znaków składa się z : ',len(x))
print ('Ciag znaków zajmuje - bytes: ',sys.getsizeof(x))

liczbaD=0xfffffffffffffff
#liczbaD=liczbaD +1
print('dla', liczbaD, 'Ciag znaków zajmuje - bytes', sys.getsizeof(liczbaD))

liczbaD=0xfffffffffffffffffffffff
print('dla', liczbaD, 'Ciag znaków zajmuje - bytes', sys.getsizeof(liczbaD))

liczbaD=0xfffffffffffffffffffffffffffffff
print('dla', liczbaD, 'Ciag znaków zajmuje - bytes', sys.getsizeof(liczbaD))

liczbaD=0xfffffffffffffffffffffffffffffffffffffff
print('dla', liczbaD, 'Ciag znaków zajmuje - bytes', sys.getsizeof(liczbaD))


print('dObiekt typu ', type(PackOfDevices), 'Obiekt zajmuje - bytes', sys.getsizeof(PackOfDevices))
arr = [1,'s4444444']
print('dObiekt typu ', type(arr), 'Obiekt zajmuje - bytes', sys.getsizeof(arr))

x= array.array('I',[1,1])

print('dObiekt typu ', type(x), 'Obiekt zajmuje - bytes', sys.getsizeof(x))