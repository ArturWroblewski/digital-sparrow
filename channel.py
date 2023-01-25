import array




class Channel:
    TypeOfData = 0  # 0-BUS, 1-Digital, 2-Analog, not use 3-Andalog&Digital
    SPS = 0  # Samples per second (44100 = 44,1khz)
    SPS = 0  # Samples per second (44100 = 44,1khz)
    sizeOfSample = 0 #Wielkość próbki od 0-64bit
    sizeOfSampleCode = 0  # Wielkość próbki od 0-64bit
    marker = 0;
    maxSizeOfArray = 0
    methodOfAdding = 0  # 0 use table 1 use RAW
    scaleOfADC = bytes([0x00, 0x05])    # jeżeli sa tylko 2 to mini i max , jezeli 3 to mini max i zero, itd..



    def __init__(self, name ,sizeOfSamples,dateStart, SPS, maxSizeOfArray):
        self.setSizeOfSample(sizeOfSamples)
        self.Name = name
        self.StartDate = dateStart
        self.SPS=SPS
        self.maxSizeOfArray = maxSizeOfArray
        self.dataStorage = list()
        self.createNewTmpArray()
        #self.tmpArray = bytearray(self.maxSizeOfArray)


    def add(self, dataToPutIn):
        key = bytes([0x13, 0x00, 0x00, 0x00, 0x08, 0x00])
        if self.methodOfAdding == 1:
            self.dataStorage.append(dataToPutIn)

        if self.methodOfAdding == 0:
            for i in dataToPutIn:
                self.tmpArray[self.marker]=i #i jest obiektem nie liczbą jak w C#
                #print('Obiekt ',i, 'wlozony w ' , self.dataStorage.__len__(), 'marer to ', self.marker)
                self.marker = self.marker+1
                if self.marker == self.maxSizeOfArray:
                    self.marker =0
                    self.dataStorage.append(self.tmpArray)
                    #del self.tmpArray
                    self.createNewTmpArray()


    def printStat(self):
        if self.methodOfAdding == 0:

            if self.dataStorage.__len__() >0:
                print('Lista posiada ', self.dataStorage.__len__(), 'Objekty typu', type(self.dataStorage.__getitem__(0)), ' o długości ' , len(self.dataStorage.__getitem__(0)),' z markerem w tabeli tymczasowej ustawionym na ', self.marker ,'. Aktualnie zebrano próbek: ', self.dataStorage.__len__()* self.maxSizeOfArray + self.marker)
            if self.dataStorage.__len__() == 0:
                print('Lista posiada ', self.dataStorage.__len__(), 'Objekty typu', type(self.tmpArray),
                    ' o długości ', len(self.tmpArray),
                    ' z markerem w tabeli tymczasowej ustawionym na ', self.marker, '. Aktualnie zebrano próbek: ',
                    self.dataStorage.__len__() * self.maxSizeOfArray + self.marker)
            print('Dane zapisane są w formie ', self.sizeOfSample , 'bit')

        if self.methodOfAdding == 1:
            if self.dataStorage.__len__() > 0:
                print('Lista posiada ', self.dataStorage.__len__(), 'Objekty typu',
                        type(self.dataStorage.__getitem__(0)), ' o długości ', len(self.dataStorage.__getitem__(0)),

                        '. Aktualnie zebrano próbek: ',
                        self.dataStorage.__len__() * len(self.dataStorage.__getitem__(0)) + self.marker)

    def printAllObject(self):
        for i in self.dataStorage:
            print(i)
        print(self.tmpArray[0:self.marker])


    def getMarker(self):
        return self.marker

    def setSizeOfSample(self, size):

        if size<8:
            self.sizeOfSample = size*8+8
            self.sizeOfSampleCode = size

    def setStorageMethode(self, codeRAW):

        if codeRAW < 2:
            self.methodOfAdding = codeRAW

    def createNewTmpArray(self):
        if self.sizeOfSampleCode==0:
            self.tmpArray = bytearray(self.maxSizeOfArray)
        if self.sizeOfSampleCode==1:
            self.tmpArray = array.array('I',(0 for i in range(0,self.maxSizeOfArray)))
        if self.sizeOfSampleCode>1 and self.sizeOfSampleCode<4:
            self.tmpArray = array.array('L',(0 for i in range(0,self.maxSizeOfArray)))
        if  self.sizeOfSampleCode > 3:
            self.tmpArray = array.array('Q', (0 for i in range(0, self.maxSizeOfArray)))

    def getTable(self,):
        print(self.tmpArray[0:self.marker])