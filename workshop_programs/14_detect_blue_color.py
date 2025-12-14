#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 5.2: Detect Blue Color

Workshop Program - Converted from Google Colab
"""

import cv2
import numpy as np

img = cv2.imread('sample.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define blue color range in HSV
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])

# Create mask for blue color
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Apply mask to original image
result = cv2.bitwise_and(img, img, mask=mask)

print("Original:")
cv2.imshow("5.2- Detect Blue Color", img)
print("\nBlue Mask:")
cv2.imshow("5.2- Detect Blue Color", mask)
print("\nBlue Objects:")
cv2.imshow("5.2- Detect Blue Color", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
