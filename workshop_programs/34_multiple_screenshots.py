#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 6.4: Multiple Screenshots (Website Comparison)

Workshop Program - Converted from Google Colab
"""

from playwright.sync_api import sync_playwright
import cv2
import numpy as np

websites = [
    ('https://www.google.com', 'google.png'),
    ('https://www.github.com', 'github.png'),
    ('https://www.python.org', 'python.png'),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    for url, filename in websites:
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path=filename)
        print(f"Saved: {filename}")
        page.close()

    browser.close()
    print("\nAll screenshots saved!")

# Display all screenshots
for _, filename in websites:
    print(f"\n{filename}:")
    img = cv2.imread(filename)
    img = cv2.resize(img, (400, 300))  # Resize for display
    cv2.imshow("6.4- Multiple Screenshots (Website Compa", img)


def google_search(query):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto('https://www.google.com')

        # Accept cookies if prompted (for some regions)
        try:
            page.click('button:has-text("Accept")', timeout=3000)
        except:
            pass

        # Type search query
        page.fill('textarea[name="q"]', query)
        page.press('textarea[name="q"]', 'Enter')

        # Wait for results
        page.wait_for_selector('#search')

        # Get search results
        results = page.locator('#search .g h3').all_text_contents()

        print(f"\n=== Search Results for '{query}' ===")
        for i, result in enumerate(results[:5], 1):
            print(f"{i}. {result}")

        # Screenshot of results
        page.screenshot(path='search_results.png')

        browser.close()

# Run the search
google_search('Python tutorials for beginners')

# Display screenshot
cv2.imshow("6.4- Multiple Screenshots (Website Compa", cv2.imread('search_results.png'))
cv2.waitKey(0)
cv2.destroyAllWindows()
