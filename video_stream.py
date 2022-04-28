import os
import cv2
from datetime import datetime
from send_images_to_db import send_images_to_firebase

cam = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('/home/tahir/Documents/DataScience/IOTProject/Videos/' + 'output.avi', fourcc, 20.0, (640, 480))
IMAGES_SAVED_PATH = '/home/tahir/Documents/DataScience/IOTProject/CapturedImages/'
PATH = "/home/tahir/Documents/DataScience/IOTProject/CapturedImages/"

# i = 0

while cam.isOpened():
    
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    out.write(frame1)

    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    _, tresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(tresh, None, iterations=3)

    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:

        if cv2.contourArea(c) < 500:
            continue

        x, y, w, h = cv2.boundingRect(c)

        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

        if cv2.rectangle is not None:

            now = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
            cv2.imwrite(IMAGES_SAVED_PATH + f"{now}" + '.jpg', frame1)
            
            f_name = now + ".jpg"
            path = PATH+f_name
            send_images_to_firebase(f_name, path)

    if cv2.waitKey(10) == ord('q'):
        break

    cv2.imshow('REAL TIME CAM', frame1)
