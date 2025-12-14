#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 4.3: Draw Circles

Workshop Program - Converted from Google Colab
"""

import cv2
import numpy as np

canvas = np.zeros((400, 600, 3), dtype=np.uint8)

# Draw circle (image, center, radius, color, thickness)
cv2.circle(canvas, (150, 200), 80, (255, 255, 0), 2)      # Outline
cv2.circle(canvas, (400, 200), 80, (255, 0, 255), -1)     # Filled

cv2.imshow("4.3- Draw Circles", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
