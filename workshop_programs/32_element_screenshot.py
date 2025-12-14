#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 6.2: Element Screenshot

Workshop Program - Converted from Google Colab
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto('https://www.python.org')

    # Screenshot of specific element
    logo = page.locator('.python-logo')
    logo.screenshot(path='python_logo.png')
    print("Logo screenshot saved!")

    browser.close()

import cv2
cv2.imshow("6.2- Element Screenshot", cv2.imread('python_logo.png'))
cv2.waitKey(0)
cv2.destroyAllWindows()
