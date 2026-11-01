from playwright.sync_api import Page

BASE_URL = "https://automationintesting.online"


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.hotel_name = page.get_by_text("Shady Meadows B&B").first
        self.check_availability_button = page.get_by_role("button", name="Check Availability")
        self.book_now_links = page.get_by_role("link", name="Book now")

    def open(self):
        self.page.goto(BASE_URL)

    def check_availability(self):
        self.check_availability_button.click()

    def book_room(self, index):
        self.book_now_links.nth(index).click()