import pytest
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

def test_search_faq_billing():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login_and_goto_help(page)
        page.fill('input[placeholder="Search"]', 'billing')
        page.click('button:has-text("Search")')
        page.wait_for_selector('text=Billing')
        assert page.is_visible('text=Billing')
        browser.close()

def test_search_faq_no_results():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login_and_goto_help(page)
        page.fill('input[placeholder="Search"]', 'fuel policy')
        page.click('button:has-text("Search")')
        assert page.is_visible('text=No FAQs found')
        browser.close()

def test_search_faq_typo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login_and_goto_help(page)
        page.fill('input[placeholder="Search"]', 'billin')
        page.click('button:has-text("Search")')
        assert page.is_visible('text=Billing')
        browser.close()
