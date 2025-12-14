#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 2.2: Open Multiple Pages (Tabs)

Workshop Program - Converted from Google Colab
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    # Create multiple pages
    page1 = browser.new_page()
    page2 = browser.new_page()
    page3 = browser.new_page()

    # Navigate each page
    page1.goto('https://www.google.com')
    page2.goto('https://www.github.com')
    page3.goto('https://www.python.org')

    print(f"Page 1: {page1.title()}")
    print(f"Page 2: {page2.title()}")
    print(f"Page 3: {page3.title()}")

    browser.close()


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto('https://demoqa.com/text-box')

    # Fill text fields
    page.fill('#userName', 'John Doe')
    page.fill('#userEmail', 'john@example.com')
    page.fill('#currentAddress', '123 Main Street')
    page.fill('#permanentAddress', '456 Park Avenue')

    # Click submit button
    page.click('#submit')

    # Take screenshot to see result
    page.screenshot(path='form_filled.png')
    print("Form filled! Screenshot saved as form_filled.png")

    browser.close()

# Display the screenshot in Colab
import cv2
img = cv2.imread('form_filled.png')
cv2.imshow("2.2- Open Multiple Pages (Tabs)", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
