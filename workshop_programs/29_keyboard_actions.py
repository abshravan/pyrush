#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 3.5: Keyboard Actions

Workshop Program - Converted from Google Colab
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto('https://www.google.com')

    # Type in search box
    page.click('textarea[name="q"]')
    page.keyboard.type('Python Playwright tutorial', delay=50)

    # Press Enter
    page.keyboard.press('Enter')
    page.wait_for_load_state('networkidle')

    page.screenshot(path='google_search.png')
    print("Search performed!")

    browser.close()

import cv2
cv2.imshow("3.5- Keyboard Actions", cv2.imread('google_search.png'))


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto('https://demoqa.com/dynamic-properties')

    # Wait for element to be visible
    page.wait_for_selector('#visibleAfter', state='visible', timeout=10000)
    print("Element is now visible!")

    page.screenshot(path='dynamic_wait.png')

    browser.close()

cv2.imshow("3.5- Keyboard Actions", cv2.imread('dynamic_wait.png'))


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto('https://quotes.toscrape.com')

    # Get all quotes
    quotes = page.locator('.quote .text').all_text_contents()
    authors = page.locator('.quote .author').all_text_contents()

    print("=== QUOTES ===")
    for i, (quote, author) in enumerate(zip(quotes, authors), 1):
        print(f"{i}. {quote}")
        print(f"   - {author}\n")

    browser.close()
cv2.waitKey(0)
cv2.destroyAllWindows()
