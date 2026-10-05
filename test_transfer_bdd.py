from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page

scenarios("features/transfer_funds.feature")


@given("the user is logged in to ParaBank")
def login(page: Page):
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    page.fill('input[name="username"]', "john")
    page.fill('input[name="password"]', "demo")
    page.click('input[value="Log In"]')
    page.wait_for_selector("text=Accounts Overview")


@given("the user is on the Transfer Funds page")
def go_to_transfer_page(page: Page):
    page.click("text=Transfer Funds")
    page.wait_for_selector("#amount")
    # Sadece ilk option'ın DOM'a eklenmesini değil,
    # listenin GERÇEKTEN dolmasını bekliyoruz.
    page.wait_for_function(
        "document.querySelectorAll('#fromAccountId option').length > 1"
    )


@when(parsers.re(r'the user transfers "(?P<amount>.*)" between two different accounts'))
def do_transfer(page: Page, amount):
    page.fill("#amount", amount)

    from_options = page.locator("#fromAccountId option").all_text_contents()
    to_options = page.locator("#toAccountId option").all_text_contents()
    print(f"From Account seçenekleri: {from_options}")
    print(f"To Account seçenekleri: {to_options}")

    from_value = from_options[0]
    # To account, from account'tan farklı olmalı
    to_value = next((v for v in to_options if v != from_value), to_options[0])
    print(f"Seçilen: from={from_value}, to={to_value}")

    page.select_option("#fromAccountId", from_value)
    page.select_option("#toAccountId", to_value)
    page.click('input[value="Transfer"]')


@then(parsers.parse('a "{message}" confirmation should be displayed'))
def verify_confirmation(page: Page, message):
    page.wait_for_selector(f"#showResult h1.title:has-text('{message}')")


@then("a validation error about the amount should be displayed")
def verify_validation_error(page: Page):
    page.wait_for_selector("#showError", timeout=10000)
    error_text = page.locator("#showError").inner_text()
    print(f"Error shown: {error_text}")
    assert page.locator("#showError h1.title").inner_text() == "Error!"