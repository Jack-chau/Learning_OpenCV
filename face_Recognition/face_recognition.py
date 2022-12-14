import numpy as np
import cv2 as cv
haar_cascade_face = cv.CascadeClassifier('haar_face.xml')
people = ['Ben Afflek','Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# features = np.load('features.npy',allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')
img = cv.imread(r'C:\Users\Jack Chau\PycharmProjects\python\python_01\OpenCV\face_Recognition\val\ben_afflek\1.jpg')
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('person',gray_img)

# Detect the face in image
face_rect = haar_cascade_face.detectMultiScale(gray_img,1.1,4)
for (x,y,w,h) in face_rect:
    faces_roi = gray_img[y:y+h,x:x+w]
    label,confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]}, with a confidence of {confidence}')

    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('Detected Face',img)
cv.waitKey(0)

