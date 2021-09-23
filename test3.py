import serial

import numpy as np
import matplotlib.pyplot as plt


ser = serial.Serial()
ser.baudrate = 9600
ser.port = "COM7"
ser.open()
count = 0
l2 = []
while True:
    i,j = 0,0
    l = []
    while i<8:
        while j<8:
            data = ser.read()
            try:
                val = int(int.from_bytes(data,"big"))
                #print(f"{data}",end="")
                if val > 100:
                    pass
                l.append(val)
            except:
                j-=1
            j+=1
        i+=1
    l2.append(l)
    count+=1
    if count == 8:
        #print(l2)
        highArea = []
        for y in range(len(l2)):
            for x in range(len(l2[y])):
                if l2[y][x] >= 26:
                    #print(x,y)
                    highArea.append((x,y))
        print(highArea)
        l2 = []
        count = 0
ser.close()