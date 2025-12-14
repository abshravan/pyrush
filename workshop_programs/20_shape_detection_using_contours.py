#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 6.5: Shape Detection using Contours

Workshop Program - Converted from Google Colab
"""

import cv2
import numpy as np

# Create image with shapes
canvas = np.zeros((400, 600, 3), dtype=np.uint8)
cv2.rectangle(canvas, (50, 50), (150, 150), (255, 255, 255), -1)
cv2.circle(canvas, (300, 100), 50, (255, 255, 255), -1)
cv2.drawContours(canvas, [np.array([[450, 50], [550, 150], [400, 150]])], 0, (255, 255, 255), -1)

gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
    x, y, w, h = cv2.boundingRect(approx)

    if len(approx) == 3:
        shape = "Triangle"
    elif len(approx) == 4:
        shape = "Rectangle"
    else:
        shape = "Circle"

    cv2.putText(canvas, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

cv2.imshow("6.5- Shape Detection using Contours", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
