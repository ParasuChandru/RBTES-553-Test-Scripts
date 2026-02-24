import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://demo.shellfleetapp.com" # Replace with actual app URL
USERNAME = "fleetmgr1"
PASSWORD = "P@ssw0rd"

def test_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f'{BASE_URL}/login')
        page.fill('input[name=email]', USERNAME)
        page.fill('input[name=password]', PASSWORD)
        page.click('button[type=submit]')
        page.wait_for_selector('text=Help Center', timeout=5000)
        assert page.is_visible('text=Help Center')
        browser.close()
