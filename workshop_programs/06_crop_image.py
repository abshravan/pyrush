#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 3.3: Crop Image

Workshop Program - Converted from Google Colab
"""

import cv2

img = cv2.imread('sample.jpg')

# Crop using array slicing [y1:y2, x1:x2]
cropped = img[50:200, 50:200]

print("Original:")
cv2.imshow("3.3- Crop Image", img)
print("\nCropped:")
cv2.imshow("3.3- Crop Image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
