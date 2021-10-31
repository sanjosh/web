from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en
    page.goto("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")

    # Click text=Language & region
    page.click("text=Language & region")
    # assert page.url == "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en"

    # Fill #c99
    page.fill("#c99", "US:en")

    # Click #c99
    page.click("#c99")

    # Click [aria-label="Update"]
    # with page.expect_navigation(url="https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en"):
    with page.expect_navigation():
        page.click("[aria-label=\"Update\"]")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
