#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 3.2: Rotate Image

Workshop Program - Converted from Google Colab
"""

import cv2

img = cv2.imread('sample.jpg')
h, w = img.shape[:2]

# Get rotation matrix (center, angle, scale)
center = (w // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)

# Apply rotation
rotated = cv2.warpAffine(img, matrix, (w, h))

print("Original:")
cv2.imshow("3.2- Rotate Image", img)
print("\nRotated 45°:")
cv2.imshow("3.2- Rotate Image", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
