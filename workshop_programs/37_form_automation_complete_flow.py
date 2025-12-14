#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program 7.4: Form Automation Complete Flow

Workshop Program - Converted from Google Colab
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto('https://demoqa.com/automation-practice-form')

    print("Filling student registration form...")

    # Personal info
    page.fill('#firstName', 'John')
    page.fill('#lastName', 'Doe')
    page.fill('#userEmail', 'john.doe@email.com')

    # Gender (radio button)
    page.click('label[for="gender-radio-1"]')

    # Mobile
    page.fill('#userNumber', '1234567890')

    # Subjects (with autocomplete)
    page.click('#subjectsInput')
    page.keyboard.type('Computer')
    page.keyboard.press('Enter')

    # Hobbies
    page.click('label[for="hobbies-checkbox-1"]')  # Sports
    page.click('label[for="hobbies-checkbox-2"]')  # Reading

    # Current Address
    page.fill('#currentAddress', '123 Test Street, Demo City')

    # Scroll and submit
    page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
    page.click('#submit')

    # Wait for confirmation modal
    page.wait_for_selector('.modal-content')

    print("Form submitted successfully!")
    page.screenshot(path='form_submitted.png')

    browser.close()

import cv2
cv2.imshow("7.4- Form Automation Complete Flow", cv2.imread('form_submitted.png'))
cv2.waitKey(0)
cv2.destroyAllWindows()
