import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.contact_form import ContactForm


VALID_VALUES = {
    "name": "Muhammad Tester",
    "email": "tester@example.com",
    "phone": "01234567890",
    "subject": "Booking question",
    "message": "Hello, I would like to ask about room availability next month.",
}


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


@pytest.mark.parametrize(
    ("field", "invalid_value", "expected_error"),
    [
        ("name", "", "Name may not be blank"),
        ("email", "not-an-email", "must be a well-formed email address"),
        ("phone", "1234567890", "Phone must be between 11 and 21 characters."),
        ("subject", "Help", "Subject must be between 5 and 100 characters."),
        ("message", "Too short message", "Message must be between 20 and 2000 characters."),
    ],
)
def test_contact_form_rejects_invalid_input(
    page: Page, field: str, invalid_value: str, expected_error: str
):
    home = HomePage(page)
    contact = ContactForm(page)
    home.open()

    values = dict(VALID_VALUES)
    values[field] = invalid_value

    contact.send_message(**values)

    expect(contact.validation_error(expected_error)).to_be_visible()
    expect(contact.success_heading(values["name"])).not_to_be_visible()


@pytest.mark.parametrize(
    ("field", "boundary_value"),
    [
        ("subject", "Hello"),
        ("message", "This message is 20ch"),
    ],
)
def test_contact_form_accepts_minimum_lengths(page: Page, field: str, boundary_value: str):
    home = HomePage(page)
    contact = ContactForm(page)
    home.open()

    values = dict(VALID_VALUES)
    values[field] = boundary_value

    contact.send_message(**values)

    expect(contact.success_heading(values["name"])).to_be_visible()