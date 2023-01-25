
import random
import slot
import time

class Device:
    ip = '0.0.0.0'
    serialNumber = 'En3Hh2YBgRfZ8QgS'
    deviceType = 0;
    #availableSlots = list() # w tym miejscu musi zostać podczas inicjalizacji wpisana nowa lista slotów. Jezeli nie bedzie przy inicjalizacji to wszystkie urzadzenia dostaną te samą listę

    def SelfTest(self):
        for i in range(random.randrange(63)):
            self.availableSlots.append(slot.Slot(random.randrange(63)))

    def __init__(self,ipAddr,SN):
        self.ip = ipAddr
        self.serialNumber = SN
        self.availableSlots = list()
        self.availableSlots.append(slot.Slot(1))
        self.SelfTest()
        print('Dodano urządzenie do listy dostępnych urządzeń.',self.ip ,' Aktualnie dostępnych slotów: ' , self.availableSlots.__len__())

    def printAvailbleSlots(self):
        for singleSlot in self.availableSlots:
            print('Numery zajętych Slotów:', singleSlot.SlotNo)

