from playwright.sync_api import sync_playwright

def test_bsa_fincen_flagging_above():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://bankapp.com/login')
        page.fill('#username', 'test_user')
        page.fill('#password', 'test_pass')
        page.click('#login-btn')

        page.goto('https://bankapp.com/wire-transfer')
        page.fill('#amount_usd', '12000')
        page.click('#submit-btn')

        assert page.is_visible('text=Transaction flagged for BSA/FinCEN reporting')
        browser.close()
