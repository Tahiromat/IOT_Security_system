import os
import cv2
from datetime import datetime
from cv2 import rectangle
from send_images_to_db import send_images_to_firebase
from send_email import email_alert
from indentify import indentify_faces

def vid_str():
    cam = cv2.VideoCapture(0)
    IMAGES_SAVED_PATH = '/home/tahir/Documents/DataScience/IOTProject/CapturedImages/'
    PATH = "/home/tahir/Documents/DataScience/IOTProject/CapturedImages/"
    i = 0
    while cam.isOpened():
        ret, frame1 = cam.read()
        ret, frame2 = cam.read()
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
                f_name = now + ".jpg"
                path = PATH+f_name
                print(f"\n\n[INFO {i}]---  {f_name} Image Captured and Saving >>> to CapturedImages\n")
                cv2.imwrite(IMAGES_SAVED_PATH + f"{now}" + '.jpg', frame1)
                print(f"[INFO {i}]---  Sending  is: {f_name}  >>> to Firebase Storage\n")
                send_images_to_firebase(f_name, path)
                print(f"[INFO {i}]---  Security Alert is Created For: {f_name}  Image\n\n\n")
                email_alert('Security problem', 'Some movements recognized', 'tahirmat@protonmail.com')
                # If image indentify then save to indentify faces folder
                indentify_faces(path)
                i += 1
        if cv2.waitKey(10) == ord('q'):
            break

        # cv2.imshow('REAL TIME CAM', frame1)
