from playwright.sync_api import sync_playwright

def test_fx_conversion_reporting():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://bankapp.com/login')
        page.fill('#username', 'test_user')
        page.fill('#password', 'test_pass')
        page.click('#login-btn')

        page.goto('https://bankapp.com/wire-transfer')
        page.fill('#amount_usd', '1500')
        page.select_option('#currency', 'EUR')
        page.click('#submit-btn')

        assert page.is_visible('text=FX Rate')
        assert page.is_visible('text=Transaction reported to Treasury')
        browser.close()
