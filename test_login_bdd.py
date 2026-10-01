from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page

scenarios("features/login.feature")


@given("the user is on the ParaBank login page")
def go_to_login_page(page: Page):
    page.goto("https://parabank.parasoft.com/parabank/index.htm")


@when("the user logs in with a valid username and password")
def login_with_valid_credentials(page: Page):
    page.fill('input[name="username"]', "john")
    page.fill('input[name="password"]', "demo")
    page.click('input[value="Log In"]')
    page.wait_for_load_state("networkidle")


@then("the Accounts Overview page should be displayed")
def verify_accounts_overview(page: Page):
    print(f"Current URL: {page.url}")
    page.screenshot(path="debug_valid_login.png")
    page.wait_for_selector("text=Accounts Overview", timeout=10000)


@when("the user attempts to log in with an invalid username and password")
def login_with_invalid_credentials(page: Page):
    page.fill('input[name="username"]', "john")
    page.fill('input[name="password"]', "WrongPassword123")
    page.click('input[value="Log In"]')


@then("an error message should be displayed")
def verify_error_message(page: Page):
    page.wait_for_load_state("networkidle")
    heading = page.locator("h1.title:visible").inner_text()
    assert "Error" in heading, f"Expected error message, but got: {heading}"


@then("the Accounts Overview page should not be displayed")
def verify_not_accounts_overview(page: Page):
    heading = page.locator("h1.title:visible").inner_text()
    assert "Accounts Overview" not in heading