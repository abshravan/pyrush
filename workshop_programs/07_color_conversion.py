#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 3.4: Color Conversion

Workshop Program - Converted from Google Colab
"""

import cv2

img = cv2.imread('sample.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert BGR to RGB (for matplotlib)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

print("Original (BGR):")
cv2.imshow("3.4- Color Conversion", img)
print("\nGrayscale:")
cv2.imshow("3.4- Color Conversion", gray)
print("\nHSV:")
cv2.imshow("3.4- Color Conversion", hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
