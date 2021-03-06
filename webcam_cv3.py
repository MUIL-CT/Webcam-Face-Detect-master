#run python webcam_cv3.py haarcascade_frontalface_default.xml

import cv2
import sys
import numpy as np
import logging as log
import datetime as dt
from time import sleep

count = 0

#cascPath = "haarcascade_frontalface_default.xml"
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)

video_capture = cv2.VideoCapture(0)
anterior = 0

while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if anterior != len(faces):
        anterior = len(faces)
        log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))

        if faces is None:
            print("none")
        else:
            if len(faces) >= 2:
                print(len(faces))
                success, image = video_capture.read()
                success = True
                if success:
                    success, image = video_capture.read()
                    
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    bottomLeftCornerOfText = (0,450)
                    fontScale = 2
                    fontColor = (255,255,255)
                    lineType = 3

                    cv2.putText(image, "#FutureReady",
                        bottomLeftCornerOfText,
                        font,
                        fontScale,
                        fontColor,
                        lineType)

                    cv2.imshow("image",image)
                    cv2.imwrite("frame%d.jpg" % count, image)           
                count += 1


    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        cv2.destroyWindow("image")    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Display the resulting frame
    cv2.imshow('Video', frame)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
