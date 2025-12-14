#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 2.2: Get Image Properties

Workshop Program - Converted from Google Colab
"""

import cv2

img = cv2.imread('sample.jpg')

print(f"Shape: {img.shape}")          # (height, width, channels)
print(f"Height: {img.shape[0]}")
print(f"Width: {img.shape[1]}")
print(f"Channels: {img.shape[2]}")    # 3 for color, 1 for grayscale
print(f"Total Pixels: {img.size}")
print(f"Data Type: {img.dtype}")