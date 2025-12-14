#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 6.3: Edge Detection (Canny)

Workshop Program - Converted from Google Colab
"""

import cv2

img = cv2.imread('sample.jpg', 0)

# Canny edge detection (lower_threshold, upper_threshold)
edges_low = cv2.Canny(img, 50, 100)
edges_med = cv2.Canny(img, 100, 200)
edges_high = cv2.Canny(img, 150, 300)

print("Original:")
cv2.imshow("6.3- Edge Detection (Canny)", img)
print("\nEdges (Low threshold):")
cv2.imshow("6.3- Edge Detection (Canny)", edges_low)
print("\nEdges (Medium threshold):")
cv2.imshow("6.3- Edge Detection (Canny)", edges_med)
print("\nEdges (High threshold):")
cv2.imshow("6.3- Edge Detection (Canny)", edges_high)
cv2.waitKey(0)
cv2.destroyAllWindows()
