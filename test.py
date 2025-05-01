from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime

# File paths
names_file_path = 'Data/names.pkl'
faces_file_path = 'Data/faces_data.pkl'
face_cascade_path = 'Data/haarcascade_frontalface_default.xml'

# Initialize camera and face detector
video = cv2.VideoCapture(0)
faces_detect = cv2.CascadeClassifier(face_cascade_path)

with open(names_file_path, 'rb') as f:
    LABELS = pickle.load(f)
with open(faces_file_path, 'rb') as f:
    FACES = pickle.load(f)

knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

background_image=cv2.imread("Background.png")

COL_NAME = ['NAME', 'TIME']

# Capture and process face frames
while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faces_detect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        crop_image = frame[y:y+h, x:x+w, :]
        resized_image = cv2.resize(crop_image, (50, 50)).flatten().reshape(1, -1)
        output=knn.predict(resized_image)
        ts=time.time()
        date=datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
        time_stamp=datetime.fromtimestamp(ts).strftime("%H:%M-%S")
        exist=os.path.isfile("Attendance/Attendance_" + date + ".csv")
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.rectangle(frame,(x,y-40),(x+w,y),(0,0,255),-1)
        cv2.putText(frame, str(output[0]), (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 2)
        attendance=[str(output[0]), str(time_stamp)]
    background_image[330:330+480, 220:220+640] = frame
    cv2.imshow("Frame", background_image)
    
    
    if cv2.waitKey(1) == ord('o'):
        if exist:
            with open("Attendance/Attendance_" + date + ".csv", "+a") as csv_file:
                writer=csv.writer(csv_file)
                writer.writerow(attendance)
                csv_file.close()
        else:
            with open("Attendance/Attendance_" + date + ".csv", "+a") as csv_file:
                writer=csv.writer(csv_file)
                writer.writerow(COL_NAME)
                writer.writerow(attendance)
                csv_file.close()
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

