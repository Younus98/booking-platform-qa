from playwright.sync_api import Page, expect

BASE_URL = "https://automationintesting.online"


def test_homepage_loads(page: Page):
    page.goto(BASE_URL)

    expect(page).to_have_url(f"{BASE_URL}/")
    expect(page.get_by_text("Shady Meadows B&B").first).to_be_visible()