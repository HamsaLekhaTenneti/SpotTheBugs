from playwright.async_api import Page
from playwright.sync_api import expect
from page_objects.spot_the_bugs import SpotTheBugs
from utils.set_form import set_form_valid_values

def test_mandatory_last_name(browser: Page):

    spot_the_bugs = SpotTheBugs(browser)
    spot_the_bugs = set_form_valid_values(spot_the_bugs)

    # Validate with no Last Name
    spot_the_bugs.last_name = ""
    spot_the_bugs.fill_and_submit()
    spot_the_bugs.validate_invalid_details()


def test_mandatory_email(browser: Page):

    spot_the_bugs = SpotTheBugs(browser)
    spot_the_bugs = set_form_valid_values(spot_the_bugs)

    # Validate with no Last Name
    spot_the_bugs.email = ""
    spot_the_bugs.fill_and_submit()
    spot_the_bugs.validate_invalid_details()