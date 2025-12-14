#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 6.5: Shape Detection using Contours - Part 2

Workshop Program - Converted from Google Colab
"""

import cv2

# Load Haar cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img = cv2.imread('face.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

print(f"Faces detected: {len(faces)}")

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(img, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

cv2.imshow("6.5- Shape Detection using Contours - Pa", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
