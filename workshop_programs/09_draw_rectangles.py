#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 4.2: Draw Rectangles

Workshop Program - Converted from Google Colab
"""

import cv2
import numpy as np

canvas = np.zeros((400, 600, 3), dtype=np.uint8)

# Draw rectangle (image, top_left, bottom_right, color, thickness)
cv2.rectangle(canvas, (50, 50), (200, 150), (0, 255, 0), 2)       # Outline
cv2.rectangle(canvas, (250, 50), (400, 150), (0, 0, 255), -1)     # Filled (-1)

cv2.imshow("4.2- Draw Rectangles", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
