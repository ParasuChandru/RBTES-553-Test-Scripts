from playwright.sync_api import sync_playwright

def test_ofac_screening_negative():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://bankapp.com/login')
        page.fill('#username', 'test_user')
        page.fill('#password', 'test_pass')
        page.click('#login-btn')

        page.goto('https://bankapp.com/wire-transfer')
        page.fill('#beneficiary_name', 'Iran Export Bank')
        page.fill('#account_number', '987654321')
        page.click('#submit-btn')

        assert page.is_visible('text=Beneficiary is sanctioned (OFAC)')
        browser.close()
