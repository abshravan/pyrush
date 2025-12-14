#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 6.3: Generate PDF

Workshop Program - Converted from Google Colab
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto('https://www.python.org')

    # Generate PDF
    page.pdf(path='python_org.pdf', format='A4', print_background=True)
    print("PDF saved! You can download it from the Files panel.")

    browser.close()