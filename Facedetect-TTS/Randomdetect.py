import cv2
import pyttsx3
import random
import numpy as np
import os
import time
import sys
import logging as log
import datetime as dt
from time import sleep
print(' ')
print(' ')
print('Press Q to exit. This program plays an alarm when it detects a face. This also takes pictures until a set amount of pictures.')
print(' ')
Webcampick = int(input('Which webcam to use? 0=default 1=secondary:'))
print(' ')
picturemax = int(input('How many pictures should this program take at maximum:'))
print(' ')
print('giving 10 seconds to get away from webcam')
time.sleep(10)


# all the =
imaget = 0
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
lines = open ('words.txt').read().splitlines()

log.basicConfig(filename='webcam.log',level=log.INFO)


video_capture = cv2.VideoCapture(Webcampick)
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
        myline = random.choice (lines)
        engine = pyttsx3.init()
        engine.say(myline)
        engine.runAndWait()
        
        if imaget < picturemax:
            cv2.imwrite('opencv'+str(imaget)+'.jpg',frame)
            imaget += 1

    if anterior != len(faces):
        anterior = len(faces)
        log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))


    # Display the resulting frame
    cv2.imshow('Video', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Display the resulting frame
    cv2.imshow('Video', frame)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
