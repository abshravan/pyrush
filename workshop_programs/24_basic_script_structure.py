#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 1.2: Basic Script Structure

Workshop Program - Converted from Google Colab
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # Must be headless=True in Colab
    page = browser.new_page()

    page.goto('https://example.com')
    print(f"Page title: {page.title()}")

    browser.close()


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Navigate to website
    page.goto('https://www.python.org')

    # Get page info
    print(f"Title: {page.title()}")
    print(f"URL: {page.url}")

    browser.close()