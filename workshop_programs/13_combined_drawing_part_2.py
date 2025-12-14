#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 4.5: Combined Drawing (Mini Project) - Part 2

Workshop Program - Converted from Google Colab
"""

import cv2
import numpy as np

img = cv2.imread('sample.jpg')
img = cv2.resize(img, (600, 400))

# Create a mask (same size as image, single channel)
mask = np.zeros(img.shape[:2], dtype=np.uint8)

# Draw white region on mask (only this area will be visible)
cv2.rectangle(mask, (100, 50), (500, 350), 255, -1)

# Apply mask
result = cv2.bitwise_and(img, img, mask=mask)

print("Original:")
cv2.imshow("4.5- Combined Drawing (Mini Project) - P", img)
print("\nMask:")
cv2.imshow("4.5- Combined Drawing (Mini Project) - P", mask)
print("\nMasked Result:")
cv2.imshow("4.5- Combined Drawing (Mini Project) - P", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
