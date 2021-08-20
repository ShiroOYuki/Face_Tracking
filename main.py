import cv2
import mediapipe as mp


class faceTracking:
    def __init__(self):
        self.mp_face_detection = mp.solutions.face_detection
        self.mp_drawing = mp.solutions.drawing_utils

        self.face_detection = self.mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.6)

    def getCap(self,h=540,w=960):
        cap = cv2.VideoCapture(0)
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


def main():
    ft = faceTracking()
    cap = ft.getCap()
    while True:
        sus,image = cap.read()
        image = ft.findFace(image,channel_reverse=True)
        cv2.imshow("image",image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()