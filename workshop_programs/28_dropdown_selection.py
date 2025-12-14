#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 3.4: Dropdown Selection

Workshop Program - Converted from Google Colab
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto('https://demoqa.com/select-menu')

    # Select from dropdown (Old Style Select)
    page.select_option('#oldSelectMenu', 'Blue')

    page.screenshot(path='dropdown.png')
    print("Dropdown selected!")

    browser.close()

import cv2
cv2.imshow("3.4- Dropdown Selection", cv2.imread('dropdown.png'))
cv2.waitKey(0)
cv2.destroyAllWindows()
