from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.contact_form import ContactForm


def test_guest_can_send_contact_message(page: Page):
    name = "Muhammad Tester"
    subject = "Booking question"

    home = HomePage(page)
    contact = ContactForm(page)

    home.open()
    contact.send_message(
        name=name,
        email="tester@example.com",
        phone="01234567890",
        subject=subject,
        message="Hello, I would like to ask about room availability next month.",
    )

    expect(contact.success_heading(name)).to_be_visible()
    expect(page.get_by_text(subject)).to_be_visible()