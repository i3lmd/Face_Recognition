import cv2
import pickle
import numpy as np
import os

# File paths
names_file_path = 'Data/names.pkl'
faces_file_path = 'Data/faces_data.pkl'
face_cascade_path = 'Data/haarcascade_frontalface_default.xml'

# Initialize camera and face detector
video = cv2.VideoCapture(0)
faces_detect = cv2.CascadeClassifier(face_cascade_path)
faces_data = []
i = 0

# Get name input
name = input("Enter your name: ")

# Capture and process face frames
while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faces_detect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        crop_image = frame[y:y+h, x:x+w, :]
        resized_image = cv2.resize(crop_image, (50, 50))
        if len(faces_data) < 100 and i % 10 == 0:
            faces_data.append(resized_image)

        i += 1
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "Face " + str(len(faces_data)), (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord('q') or len(faces_data) == 100:
        break

video.release()
cv2.destroyAllWindows()

# Convert face data to numpy and reshape
faces_data = np.asarray(faces_data)
faces_data = faces_data.reshape(100, -1)

# Handle names.pkl
if not os.path.exists(names_file_path):
    names = [name] * 100
else:
    with open(names_file_path, 'rb') as f:
        names = pickle.load(f)
    names += [name] * 100

with open(names_file_path, 'wb') as f:
    pickle.dump(names, f)

# Handle faces_data.pkl
if not os.path.exists(faces_file_path):
    with open(faces_file_path, 'wb') as f:
        pickle.dump(faces_data, f)
else:
    with open(faces_file_path, 'rb') as f:
        faces = pickle.load(f)
    faces = np.append(faces, faces_data, axis=0)
    with open(faces_file_path, 'wb') as f:
        pickle.dump(faces, f)
