#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 3.3: Checkbox and Radio Buttons

Workshop Program - Converted from Google Colab
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto('https://demoqa.com/checkbox')

    # Click on checkbox
    page.click('label[for="tree-node-home"]')

    page.screenshot(path='checkbox.png')
    print("Checkbox clicked!")

    browser.close()

import cv2
cv2.imshow("3.3- Checkbox and Radio Buttons", cv2.imread('checkbox.png'))
cv2.waitKey(0)
cv2.destroyAllWindows()
