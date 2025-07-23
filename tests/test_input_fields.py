from playwright.async_api import Page
from playwright.sync_api import expect
from page_objects.spot_the_bugs import SpotTheBugs
from utils.set_form import set_form_valid_values

def test_email(browser: Page):
    """
    Email should always have @ and domain
    """
    spot_the_bugs = SpotTheBugs(browser)

    # With Invalid email
    spot_the_bugs = set_form_valid_values(spot_the_bugs)
    spot_the_bugs.email = "ggsggg"
    spot_the_bugs.fill_and_submit()
    spot_the_bugs.validate_invalid_details()

def test_phonenumber_length(browser: Page):
    """
    Phone number must not have numbers less than 10 digits
    """
    spot_the_bugs = SpotTheBugs(browser)

    # With invalid phonenumber length
    spot_the_bugs = set_form_valid_values(spot_the_bugs)
    spot_the_bugs.phone = "7667635"
    spot_the_bugs.fill_and_submit()
    spot_the_bugs.validate_invalid_details()
    expect(spot_the_bugs.page.get_by_text("The phone number should contain at least 10 characters!")).to_be_visible()

def test_alpha_phonenumber(browser: Page):
    """
    Phone number should never access alpha numeric
    """
    spot_the_bugs = SpotTheBugs(browser)

    # With invalid phonenumber having alpha numeric
    spot_the_bugs = set_form_valid_values(spot_the_bugs)
    spot_the_bugs.phone = "ggahkhdgghshjjj"
    spot_the_bugs.fill_and_submit()
    spot_the_bugs.validate_invalid_details()


def test_password_length(browser: Page):
    """
    Test Password Field
    """
    spot_the_bugs = SpotTheBugs(browser)

    # With no password submit
    spot_the_bugs = set_form_valid_values(spot_the_bugs)
    spot_the_bugs.phone = "ddddj"
    spot_the_bugs.fill_and_submit()
    expect(spot_the_bugs.page.get_by_text("The phone number should contain at least 10 characters!")).to_be_visible()
