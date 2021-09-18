import module
import cv2
import matplotlib.pyplot as plt
import os

faceDetection = module.faceTracking()
#cap=cv2.VideoCapture(2,cv2.CAP_DSHOW)
cap=cv2.VideoCapture(2)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,540)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,960)
sus,image = cap.read()


#x,y = input("\n\nx,y:").split(",")

for i in range(1,9,1):
    for j in range(1,9,1):
        print(i,j,j+i-1)
        x,y = i-1,j-1
        image2 = faceDetection.getArea(image,(x,y))
        plt.subplot(8,8,i+8*(j-1)).imshow(image2[:,:,::-1])

plt.show()

#cv2.imshow("image",image)