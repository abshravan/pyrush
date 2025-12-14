#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 3.2: Click Elements

Workshop Program - Converted from Google Colab
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto('https://demoqa.com/buttons')

    # Different click methods
    page.dblclick('#doubleClickBtn')      # Double click
    page.click('#rightClickBtn', button='right')  # Right click
    page.click('button:has-text("Click Me"):not(#doubleClickBtn):not(#rightClickBtn)')  # Regular click

    page.screenshot(path='buttons_clicked.png')
    print("Buttons clicked! Screenshot saved.")

    browser.close()

# Display result
import cv2
cv2.imshow("3.2- Click Elements", cv2.imread('buttons_clicked.png'))
cv2.waitKey(0)
cv2.destroyAllWindows()
