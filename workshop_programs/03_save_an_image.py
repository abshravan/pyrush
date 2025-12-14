#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 2.3: Save an Image

Workshop Program - Converted from Google Colab
"""

import cv2

img = cv2.imread('sample.jpg')

# Save as different format
cv2.imwrite('output.png', img)
print("Image saved successfully!")

# In Colab, you can download the file from the Files panel on the left