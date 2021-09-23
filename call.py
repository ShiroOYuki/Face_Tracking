
import cv2
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

highArea = [(4, 0), (5, 0), (3, 1), (4, 1), (6, 1), (2, 2), (3, 2), (5, 2), (1, 3), (2, 3), (4, 3), (0, 4), (1, 4), (3, 4), (0, 5), (2, 5), (1, 6), (0, 7)]
for i in range(1,9,1):
    for j in range(1,9,1):
        if (i,j) in highArea:
            image2 = getArea(image,(i,j))
            plt.subplot(8,8,i+8*(j-1)).imshow(image2[:,:,::-1])

plt.show()

#cv2.imshow("image",image)