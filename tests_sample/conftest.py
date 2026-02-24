import pytest
from playwright.sync_api import sync_playwright

BANKING_URL = "https://demo-bank-app/"

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(BANKING_URL)
    yield page
    context.close()

def demo_login(page, username="usertest", password="password123"):
    page.fill("#username", username)
    page.fill("#password", password)
    page.click("button:has-text('Login')")
    page.wait_for_selector("#dashboard", timeout=5000)
