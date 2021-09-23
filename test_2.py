import serial
import cv2
import numpy as np
import matplotlib.pyplot as plt

#cap=cv2.VideoCapture(2,cv2.CAP_DSHOW)
cap=cv2.VideoCapture(2)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,540)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,960)
sus,image = cap.read()


#x,y = input("\n\nx,y:").split(",")

"""
for i in range(1,9,1):
    for j in range(1,9,1):
        print(i,j,j+i-1)
        x,y = i-1,j-1
        image2 = faceDetection.getArea(image,(x,y))
        plt.subplot(8,8,i+8*(j-1)).imshow(image2[:,:,::-1])
plt.show()
"""

def getArea(image,position:tuple):
        wLen=len(image[0])
        hLen=len(image)
        
        x1 = int(position[1]*hLen/9)
        x2 = int((position[1]+1)*hLen/9)
        
        y1 = int(position[0]*wLen/9)
        y2 = int((position[0]+1)*wLen/9)
        print(x1,x2,y1,y2)
        return image[x1:x2,y1:y2]
#cv2.imshow("image",image)

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
                if val > 100:
                    #print(f"\r{data}")
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
                    print(x,y)
                    highArea.append((x,y))
        l2 = []
        count = 0
       
        for i in range(1,9,1):
            for j in range(1,9,1):
                if (i,j) in highArea:
                    image2 = getArea(image,(i,j))
                    plt.subplot(8,8,i+8*(j-1)).imshow(image2[:,:,::-1])

        plt.show()

ser.close()