from playwright.sync_api import sync_playwright

def test_login_shows_account_overview():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Given: user is on the login page
        page.goto("https://parabank.parasoft.com/parabank/index.htm")

        # When: user logs in with valid credentials
        page.fill('input[name="username"]', "john")
        page.fill('input[name="password"]', "demo")
        page.click('input[value="Log In"]')

        # Then: the Accounts Overview page should be displayed
        page.wait_for_selector("text=Accounts Overview")
        print("Login successful, Accounts Overview page displayed")

        browser.close()

test_login_shows_account_overview()