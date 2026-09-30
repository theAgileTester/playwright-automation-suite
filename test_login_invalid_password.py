from playwright.sync_api import sync_playwright

def test_login_fails_with_invalid_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Given: user is on the login page
        page.goto("https://parabank.parasoft.com/parabank/index.htm")

        # When: user attempts to log in with a valid username but wrong password
        page.fill('input[name="username"]', "bonnie")
        page.fill('input[name="password"]', "WrongPassword123")
        page.click('input[value="Log In"]')

        # Then: an "Error!" heading should be shown, not Accounts Overview
        page.wait_for_selector("h1.title:visible")
        heading = page.locator("h1.title:visible").inner_text()
        print(f"Heading shown: {heading}")

        assert "Error" in heading
        assert "Accounts Overview" not in heading

        browser.close()

test_login_fails_with_invalid_password()
