#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 7.2: Login Automation (Demo Site)

Workshop Program - Converted from Google Colab
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Navigate to demo login page
    page.goto('https://the-internet.herokuapp.com/login')

    print("Filling login form...")

    # Fill username and password
    page.fill('#username', 'tomsmith')
    page.fill('#password', 'SuperSecretPassword!')

    # Click login button
    page.click('button[type="submit"]')

    # Wait for navigation
    page.wait_for_url('**/secure')

    # Verify login success
    success_message = page.locator('.flash.success').text_content()
    print(f"Login Result: {success_message.strip()}")

    # Take screenshot
    page.screenshot(path='login_success.png')

    browser.close()

import cv2
cv2.imshow("7.2- Login Automation (Demo Site)", cv2.imread('login_success.png'))
cv2.waitKey(0)
cv2.destroyAllWindows()
