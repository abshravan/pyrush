#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 5.2: Extract Links

Workshop Program - Converted from Google Colab
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto('https://www.python.org')

    # Get all links
    links = page.locator('a').all()

    print("=== LINKS ON PYTHON.ORG ===")
    for i, link in enumerate(links[:10], 1):  # First 10 links
        href = link.get_attribute('href')
        text = link.text_content().strip()
        if text and href:
            print(f"{i}. {text[:50]} -> {href[:60]}")

    browser.close()