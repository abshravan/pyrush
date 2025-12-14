#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 6.4: Find and Draw Contours

Workshop Program - Converted from Google Colab
"""

import cv2

img = cv2.imread('sample.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply threshold
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw all contours
img_contours = img.copy()
cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)

print(f"Total contours found: {len(contours)}")

print("\nOriginal:")
cv2.imshow("6.4- Find and Draw Contours", img)
print("\nThreshold:")
cv2.imshow("6.4- Find and Draw Contours", thresh)
print("\nContours:")
cv2.imshow("6.4- Find and Draw Contours", img_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()
