import pytest
import time
from playwright.sync_api import sync_playwright

BASE_URL = "https://demo.shellfleetapp.com"
USERNAME = "fleetmgr1"
PASSWORD = "P@ssw0rd"

def login_and_goto_help(page):
    page.goto(f'{BASE_URL}/login')
    page.fill('input[name=email]', USERNAME)
    page.fill('input[name=password]', PASSWORD)
    page.click('button[type=submit]')
    page.wait_for_selector('text=Help Center')
    page.click('text=Help Center')

def test_help_response_time():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login_and_goto_help(page)
        start = time.time()
        page.reload()
        page.wait_for_selector('text=Help Center')
        elapsed = time.time() - start
        assert elapsed < 2, f'Response time was {elapsed}'
        browser.close()

def test_help_availability_many_times():
    fail_count = 0
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        for i in range(10):
            try:
                login_and_goto_help(page)
            except Exception:
                fail_count += 1
        assert fail_count <= 1
        browser.close()

def test_backend_outage():
    # This is illustrative, as actual error simulation would require backend manipulation or API mock
    pass  # Placeholder
