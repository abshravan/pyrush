#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 2.3: Save an Image - Part 2

Workshop Program - Converted from Google Colab
"""

import cv2

img = cv2.imread('sample.jpg')

# Resize to specific dimensions
resized = cv2.resize(img, (400, 300))

# Resize by scale factor
scaled = cv2.resize(img, None, fx=0.5, fy=0.5)

print("Original:")
cv2.imshow("2.3- Save an Image - Part 2", img)
print("\nResized (400x300):")
cv2.imshow("2.3- Save an Image - Part 2", resized)
print("\nScaled 50%:")
cv2.imshow("2.3- Save an Image - Part 2", scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()
