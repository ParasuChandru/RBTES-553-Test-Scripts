import pytest
from playwright.sync_api import sync_playwright

def test_ofac_screening_positive():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://bankapp.com/login")
        page.fill("#username", "test_user")
        page.fill("#password", "test_pass")
        page.click("#login-btn")

        page.goto("https://bankapp.com/wire-transfer")
        page.fill("#beneficiary_name", "John Doe")
        page.fill("#account_number", "123456789")
        page.click("#submit-btn")

        assert page.is_visible("text=Transfer Submitted Successfully")
        browser.close()
