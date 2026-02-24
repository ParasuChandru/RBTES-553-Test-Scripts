import time
from playwright.sync_api import sync_playwright

def test_wire_transfer_performance():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://bankapp.com/login')
        page.fill('#username', 'test_user')
        page.fill('#password', 'test_pass')
        page.click('#login-btn')

        page.goto('https://bankapp.com/wire-transfer')
        page.fill('#amount_usd', '1000')
        page.select_option('#currency', 'INR')
        start_time = time.time()
        page.click('#submit-btn')
        page.wait_for_selector('text=Transfer Submitted Successfully')
        end_time = time.time()
        assert (end_time - start_time) <= 5
        browser.close()
