from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.contact_form import ContactForm


def test_guest_can_send_contact_message(page: Page):
    home = HomePage(page)
    contact = ContactForm(page)

    home.open()
    contact.send_message(
        name="Muhammad Tester",
        email="tester@example.com",
        phone="01234567890",
        subject="Booking question",
        message="Hello, I would like to ask about room availability next month.",
    )

    expect(page.get_by_text("Muhammad Tester")).to_be_visible()