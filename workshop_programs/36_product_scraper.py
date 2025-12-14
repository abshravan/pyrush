#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 7.3: Product Scraper

Workshop Program - Converted from Google Colab
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto('https://books.toscrape.com')

    print("=== BOOKS SCRAPER ===\n")

    # Get all books
    books = page.locator('article.product_pod').all()

    for i, book in enumerate(books[:10], 1):
        title = book.locator('h3 a').get_attribute('title')
        price = book.locator('.price_color').text_content()
        rating = book.locator('p.star-rating').get_attribute('class').split()[-1]

        print(f"{i}. {title}")
        print(f"   Price: {price}")
        print(f"   Rating: {rating} stars\n")

    browser.close()