#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 5.3: Color Detection with Sliders (Colab Version)

**Note:** Since Colab doesn't support cv2 trackbars, we use ipywidgets instead. - Part 2

Workshop Program - Converted from Google Colab
"""

import cv2
import numpy as np

img = cv2.imread('sample.jpg')

# Different blur techniques
blur_avg = cv2.blur(img, (5, 5))                    # Average blur
blur_gaussian = cv2.GaussianBlur(img, (5, 5), 0)    # Gaussian blur
blur_median = cv2.medianBlur(img, 5)                # Median blur (good for noise)

print("Original:")
cv2.imshow("5.3- Color Detection with Sliders (Colab", img)
print("\nAverage Blur:")
cv2.imshow("5.3- Color Detection with Sliders (Colab", blur_avg)
print("\nGaussian Blur:")
cv2.imshow("5.3- Color Detection with Sliders (Colab", blur_gaussian)
print("\nMedian Blur:")
cv2.imshow("5.3- Color Detection with Sliders (Colab", blur_median)
cv2.waitKey(0)
cv2.destroyAllWindows()
