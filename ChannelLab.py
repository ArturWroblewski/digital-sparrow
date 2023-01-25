import channel
import time
import array

kanal = channel.Channel('Kanala1',1,time.time(),44100,1024)
key = bytes([0x13, 0xff, 0xff, 0xff, 0x08, 0xff,0x01])
for i in range(0,100000):
    kanal.add(key)




kanal.printAllObject()
kanal.printStat()
time.sleep(10)

