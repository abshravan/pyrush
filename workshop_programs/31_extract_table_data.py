#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 5.3: Extract Table Data

Workshop Program - Converted from Google Colab
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto('https://demoqa.com/webtables')

    # Get table rows
    rows = page.locator('.rt-tr-group').all()

    print("=== TABLE DATA ===")
    for row in rows:
        cells = row.locator('.rt-td').all_text_contents()
        if cells[0]:  # If row has data
            print(f"Name: {cells[0]} {cells[1]}, Email: {cells[3]}")

    browser.close()


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto('https://www.python.org')

    # Full page screenshot
    page.screenshot(path='python_org_full.png', full_page=True)
    print("Full page screenshot saved!")

    # Viewport screenshot only
    page.screenshot(path='python_org_viewport.png')
    print("Viewport screenshot saved!")

    browser.close()

# Display viewport screenshot
import cv2
cv2.imshow("5.3- Extract Table Data", cv2.imread('python_org_viewport.png'))
cv2.waitKey(0)
cv2.destroyAllWindows()
