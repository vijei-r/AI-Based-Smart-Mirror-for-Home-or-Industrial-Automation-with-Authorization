import time
import numpy as np
import face_recognition
import os
import cvzone.HandTrackingModule as ch
import cv2 as cv
import pyautogui as pa
from ultralytics import YOLO
import mouse
import voiceCommand as ai
import gui as b
import threading
import serial
import firebase as fg
# import GestureControl as gc
port = 'COM3'
ser = serial.Serial(port, 9600)
tracking = ch.HandDetector(maxHands=1,detectionCon=0.5,minTrackCon=0.5)
width,height=pa.size()
path = 'images'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
#print(classNames)
def ultra():
    data = int(ser.readline())
    return data

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


encodeListKnown = findEncodings(images)
print('Encoding Complete')
cap = cv.VideoCapture(0)
def Gesture():
    success, imgg = cap.read()
    flipimg = cv.flip(imgg, 1)
    imgg = tracking.findHands(flipimg, draw=True)
    lmList, bbox = tracking.findPosition(imgg, draw=True)
    # print(lmList)

    if lmList:
        finger = tracking.fingersUp()
        print(finger)
        x1, y1 = lmList[8][1], lmList[8][2]
        x2, y2 = lmList[12][1], lmList[12][2]
        x4, y4 = lmList[4][1], lmList[4][2]
        x3 = (np.interp(x1, (150, 640 - 150), (10, width)))  ###100
        y3 = (np.interp(y1, (150, 480 - 150), (10, height)))  #### 150
        if finger[1] == 1 and finger[2] == 0 and finger[3] == 0 and finger[4] == 0:
            fg.ref.update({'float': 1})
            length, img, _ = tracking.findDistance(17, 4, imgg, draw=True)
            # length = length
            # print(length)
            if length > 150:
                fg.ref.update({'int': 175})
            elif length > 110 and length < 150:
                fg.ref.update({'int': 130})
            elif length > 80 and length < 110:
                fg.ref.update({'int': 65})
            elif length < 80:
                fg.ref.update({'int': 0})
        elif finger[1] == 1 and finger[2] == 1 and finger[3] == 0 and finger[4] == 0:
            fg.ref.update({'float': 0})
        elif finger[0] == 0 and finger[1] == 0 and finger[2] == 0 and finger[3] == 0 and finger[4] == 0:
            return "none"


    cv.waitKey(1)
    #cv.imshow("image", imgg)
model = YOLO('model.pt')
def process():
    while True:
        data = int(ser.readline())
        print(data)
        # if data < 50:
        #     print(data)
        success, img = cap.read()
        # img = captureScreen()
        imgS = cv.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv.cvtColor(imgS, cv.COLOR_BGR2RGB)
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)
            # print(matchIndex)
            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                print(name)
                if name == "RISHI" and data < 50:
                    print(name)
                    b.c=0
                    b.p=0
                    ai.c=0
                    threading.Thread(target=b.rishi).start()
                    threading.Thread(target=b.N).start()
                    threading.Thread(target=b.v).start()
                    threading.Thread(target=ai.main).start()
                    while True:
                        a=Gesture()
                        if a == "none":
                            print(a)
                            b.c = 1
                            b.p=1
                            ai.c=1
                            time.sleep(5)
                            break
                elif name == "NISHANTH"and data < 50:
                    print(name)
                    b.c = 0
                    b.p = 0
                    ai.c = 0
                    threading.Thread(target=b.rishi).start()
                    threading.Thread(target=b.N).start()
                    threading.Thread(target=b.v).start()
                    threading.Thread(target=ai.main).start()
                    while True:
                        a = Gesture()
                        if a == "none":
                            print(a)
                            b.c = 1
                            b.p = 1
                            ai.c = 1
                            time.sleep(5)
                            break
                else:
                    continue
            elif data < 50:
                print("none")
                b.c = 0
                b.p = 0
                threading.Thread(target=b.N).start()
                threading.Thread(target=b.v).start()
                threading.Thread(target=b.calen).start()
                threading.Thread(target=b.NR).start()
                while True:
                    data1 = int(ser.readline())
                    print("loop"+" "+str(data1))
                    if data1 >50:
                        b.c = 1
                        b.p = 1
                        break
        threading.Thread(target=b.none).start()
        #cv.imshow('Webcam', img)
        cv.waitKey(1)


def destroy():
    cap.release()
    cv.destroyAllWindows()
threading.Thread(target=process).start()
b.window.mainloop()


