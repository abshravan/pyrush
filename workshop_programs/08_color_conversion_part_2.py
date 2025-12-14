#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 3.4: Color Conversion - Part 2

Workshop Program - Converted from Google Colab
"""

import cv2
import numpy as np

# Create blank canvas (black image)
canvas = np.zeros((400, 600, 3), dtype=np.uint8)

# Draw line (image, start_point, end_point, color, thickness)
cv2.line(canvas, (50, 50), (550, 50), (0, 255, 0), 3)      # Green
cv2.line(canvas, (50, 100), (550, 100), (0, 0, 255), 5)    # Red
cv2.line(canvas, (50, 150), (550, 150), (255, 0, 0), 2)    # Blue

cv2.imshow("3.4- Color Conversion - Part 2", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
