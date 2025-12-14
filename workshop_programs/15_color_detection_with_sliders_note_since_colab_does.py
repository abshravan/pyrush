#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 5.3: Color Detection with Sliders (Colab Version)

**Note:** Since Colab doesn't support cv2 trackbars, we use ipywidgets instead.

Workshop Program - Converted from Google Colab
"""

import cv2
import numpy as np
import ipywidgets as widgets
from IPython.display import display, clear_output

img = cv2.imread('sample.jpg')

def detect_color(l_h, l_s, l_v, u_h, u_s, u_v):
    clear_output(wait=True)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([l_h, l_s, l_v])
    upper = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    # Stack images horizontally for comparison
    combined = np.hstack([img, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR), result])
    cv2.imshow("5.3- Color Detection with Sliders (Colab", combined)

# Create interactive sliders
widgets.interact(detect_color,
    l_h=widgets.IntSlider(min=0, max=179, value=0, description='Lower H'),
    l_s=widgets.IntSlider(min=0, max=255, value=50, description='Lower S'),
    l_v=widgets.IntSlider(min=0, max=255, value=50, description='Lower V'),
    u_h=widgets.IntSlider(min=0, max=179, value=10, description='Upper H'),
    u_s=widgets.IntSlider(min=0, max=255, value=255, description='Upper S'),
    u_v=widgets.IntSlider(min=0, max=255, value=255, description='Upper V')
)
cv2.waitKey(0)
cv2.destroyAllWindows()
