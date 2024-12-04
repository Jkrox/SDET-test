"""
My first test suite for this simple project.
The approach is to use Playwright to make automated tests.
"""

import pytest
from playwright.sync_api import sync_playwright

def test_word_counter() -> None:
    with sync_playwright() as p:
        # I'm interested in open the browser to see the test running, so we pass `headless=False`
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://wordcounter.net/")

        # Input test
        text = "This is a test. This is only a test."
        # First commit / test