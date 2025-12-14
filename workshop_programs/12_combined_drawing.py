#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 4.5: Combined Drawing (Mini Project)

Workshop Program - Converted from Google Colab
"""

import cv2
import numpy as np

canvas = np.zeros((500, 700, 3), dtype=np.uint8)

# Draw a simple house
cv2.rectangle(canvas, (200, 250), (500, 450), (0, 165, 255), -1)  # House body
cv2.line(canvas, (150, 250), (350, 100), (0, 0, 200), 5)          # Roof left
cv2.line(canvas, (550, 250), (350, 100), (0, 0, 200), 5)          # Roof right
cv2.line(canvas, (150, 250), (550, 250), (0, 0, 200), 5)          # Roof base
cv2.rectangle(canvas, (300, 320), (400, 450), (139, 69, 19), -1)  # Door
cv2.circle(canvas, (380, 390), 8, (255, 215, 0), -1)              # Door knob
cv2.rectangle(canvas, (220, 280), (280, 340), (255, 255, 0), -1)  # Window
cv2.putText(canvas, 'My House', (270, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 2)

cv2.imshow("4.5- Combined Drawing (Mini Project)", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
