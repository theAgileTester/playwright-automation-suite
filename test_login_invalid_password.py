from playwright.sync_api import sync_playwright

def test_login_fails_with_invalid_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Given: user is on the login page
        page.goto("https://parabank.parasoft.com/parabank/index.htm")

        # When: user attempts to log in with a valid username but wrong password
        page.fill('input[name="username"]', "john")
        page.fill('input[name="password"]', "WrongPassword123")
        page.click('input[value="Log In"]')

        page.wait_for_load_state("networkidle")
        print(f"Current URL: {page.url}")
        page.screenshot(path="debug_login_attempt.png")

        heading = page.locator("h1.title:visible").inner_text()
        print(f"Heading shown: {heading}")

        assert "Error" in heading, (
            f"DEFECT: invalid credentials were not rejected — app showed '{heading}' instead of an error"
        )

        browser.close()

test_login_fails_with_invalid_password()