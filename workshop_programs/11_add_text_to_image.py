#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 4.4: Add Text to Image

Workshop Program - Converted from Google Colab
"""

import cv2
import numpy as np

canvas = np.zeros((400, 600, 3), dtype=np.uint8)

# Put text (image, text, position, font, scale, color, thickness)
cv2.putText(canvas, 'Hello OpenCV!', (100, 100),
            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)

cv2.putText(canvas, 'Python Workshop', (100, 200),
            cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2)

cv2.imshow("4.4- Add Text to Image", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
