from playwright.sync_api import sync_playwright

def test_playwright_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://playwright.dev/python/")
        title = page.title()
        print(f"Page title: {title}")
        assert "Playwright" in title
        browser.close()

test_playwright_homepage()
