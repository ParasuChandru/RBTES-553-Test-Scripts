import pytest
from playwright.sync_api import sync_playwright

def test_missing_required_field():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://your-app-url/login')
        page.fill('#username', 'valid_user')
        page.fill('#password', 'valid_pass')
        page.click('#login')
        page.goto('https://your-app-url/rbtes-553-feature')
        page.fill('#name', '')
        page.fill('#age', '25')
        page.click('#submit')
        assert 'Name is required' in page.inner_text('.error')
        browser.close()
