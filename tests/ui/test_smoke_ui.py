from playwright.sync_api import Page, expect
from pages.home_page import HomePage


def test_homepage_loads(page: Page):
    home = HomePage(page)
    home.open()

    expect(home.hotel_name).to_be_visible()