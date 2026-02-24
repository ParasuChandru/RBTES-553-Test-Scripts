import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://demo.shellfleetapp.com"
USERNAME = "fleetmgr1"
PASSWORD = "P@ssw0rd"
CATEGORIES = ['Card Management', 'Billing', 'Compliance', 'Lost/Stolen']

def test_access_faq_categories():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f'{BASE_URL}/login')
        page.fill('input[name=email]', USERNAME)
        page.fill('input[name=password]', PASSWORD)
        page.click('button[type=submit]')
        page.wait_for_selector('text=Help Center')
        page.click('text=Help Center')
        for cat in CATEGORIES:
            assert page.is_visible(f'text={cat}')
            page.click(f'text={cat}')
            assert page.locator('.faq-answer').is_visible()
        browser.close()

def test_access_faq_logged_out_redirect():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f'{BASE_URL}/help')
        assert '/login' in page.url
        browser.close()
