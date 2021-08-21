import os
import cv2
import mediapipe as mp
import time
import numpy as np
import matplotlib.pyplot as plt


class faceTracking:
    def __init__(self):
        self.mp_face_detection = mp.solutions.face_detection
        self.mp_drawing = mp.solutions.drawing_utils

        self.face_detection = self.mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.6)

    def getCap(self,h=540,w=960,camera=0):
        cap = cv2.VideoCapture(camera)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT,h)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH,w)
        return cap

    def findFace(self,image,draw = True,channel_reverse=False):
        if channel_reverse:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        self.results = self.face_detection.process(image)
        
        if channel_reverse:
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        if self.results.detections and draw:
            for detection in self.results.detections:
                self.mp_drawing.draw_detection(image,detection)
        return image

    def getScale(self):
        if self.results.detections:
            Lms = []
            for detection in self.results.detections:
                location = detection.location_data
                #get field
                if location.HasField('relative_bounding_box'):
                    relative_bounding_box = location.relative_bounding_box
                    xmin = relative_bounding_box.xmin
                    ymin = relative_bounding_box.ymin
                    width = relative_bounding_box.width
                    height = relative_bounding_box.height
                    box = [xmin,ymin,width,height]
                    Lms.append(box)
                # get keypoint
                for keypoint in location.relative_keypoints:
                    Lms.append([keypoint.x,keypoint.y])
            return Lms
        return

    def ScaleToPos(self,image,LmsScale,Precision = False):
        h,w,c = image.shape
        for i in LmsScale:
            for j in range(len(i)):
                if j%2 == 0:
                    i[j] *= w
                else:
                    i[j] *= h
                if not Precision:
                    i[j] = int(i[j])
                if i[j] <0:
                    i[j] = 0
        return LmsScale

def main():
    ft = faceTracking()
    cap = ft.getCap(camera=0)
    cTime = 0
    pTime = 0
    getFpsTime = 0
    
    while True:
        sus,image = cap.read()
        image = ft.findFace(image,channel_reverse=True)
        LmsScale = ft.getScale()
        
        # face zoom in
        if LmsScale:
            LmsPos = ft.ScaleToPos(image,LmsScale)
            if LmsPos:
                box = LmsPos[0]
                image = image[box[1]:box[1]+box[3],box[0]:box[0]+box[2]]
                # resize
                image = cv2.resize(image,None,fx = 2,fy = 2)

        # get fps
        cTime = time.time()
        if time.time()-getFpsTime >= 1:
            fps = int(1/(cTime-pTime))
            getFpsTime = time.time()
        pTime = cTime
        
        cv2.putText(image,f"FPS:{str(fps)}",(10,30),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255))


        cv2.imshow("image",image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()