#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 6.2: Thresholding

Workshop Program - Converted from Google Colab
"""

import cv2

img = cv2.imread('sample.jpg', 0)  # Load as grayscale

# Binary thresholding
_, thresh_binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, thresh_binary_inv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

# Adaptive thresholding (better for uneven lighting)
thresh_adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY, 11, 2)

print("Original:")
cv2.imshow("6.2- Thresholding", img)
print("\nBinary:")
cv2.imshow("6.2- Thresholding", thresh_binary)
print("\nBinary Inverted:")
cv2.imshow("6.2- Thresholding", thresh_binary_inv)
print("\nAdaptive:")
cv2.imshow("6.2- Thresholding", thresh_adaptive)
cv2.waitKey(0)
cv2.destroyAllWindows()
