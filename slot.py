import time

class Slot:
    SlotNo = 0      # 0-63, Slot 0 is not removable it the base device
    removable = 0   # 0-not-removable, 1-removable
    TypeOfData = 0  # 0-BUS, 1-Digital, 2-Analog, 3-Andalog&Digital
    serialNumber = 'JOmWi3p6FEZp22pg'
    TypeOfCard = 'JapezTULBhwH8C'

    samplesInPackage = 0
    availableAnalogChannels = 0
    availableDigitalChannels = 0
    availableBUSChannels = 0

    def SetTypeOfSlot(self,TypeNo):
        self.TypeOfData = TypeNo

    def __init__(self, number):
        self.SlotNo = number

    def add(self, number):
        print('Dodaj dane. Znacznik ustalony na:', time.time())

    def getLastRead(self,numberOfRead):
        print('Zwroc ostatnie pomiay w liczbie:'+numberOfRead)

    def getSerialNumber(self):
        print('SN modulee is',self.serialNumber)
