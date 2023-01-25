
import random
import string
import device
import slot
import socket






class Devices:
    ip='10.1.0.31'
    availableDevices = list()

    #availableDevices.append(Device())
    def getLocalIP(self):
        print('Local IP Addr:')
    def getSubnetMask(self):
        print('Local Subnet Mask:')
    def setEthernetInterface(self):
        print('Eth0')
    def getListOfEthernetInterface(self):
        print('Eth0')
    def echoDevice(self):
        print('Eth0')
    def ShearchDevices(self):
        print('Eth0')
    def printDevices(self):
        for i in range(self.availableDevices.__len__()):
            print('Urządzeńie SN:', self.availableDevices.__getitem__(i).serialNumber , 'IP:', self.availableDevices.__getitem__(i).ip)
    def shearchDevicesTets(self):
        for i in range(random.randrange(255)):
            self.availableDevices.append(device.Device('123.121.123.' + str(random.randrange(255)), ''.join(
                [random.choice(string.ascii_letters + string.digits) for n in range(32)])))
    def printAvailbleDevices(self):
        for availbleDevice in self.availableDevices:
            print('Dostępne urządzenie:', availbleDevice.ip)

