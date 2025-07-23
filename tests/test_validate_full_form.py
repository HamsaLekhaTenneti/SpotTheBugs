from playwright.async_api import Page
from playwright.sync_api import expect
from page_objects.spot_the_bugs import SpotTheBugs
from utils.set_form import set_form_valid_values

def test_with_valid_form_details(browser: Page):
    """
    This is to validate form details when all the values are written correctly
    """
    spot_the_bugs = SpotTheBugs(browser)
    spot_the_bugs = set_form_valid_values(spot_the_bugs)
    spot_the_bugs.fill_and_submit()
    spot_the_bugs.validate_success_message()
    spot_the_bugs.validate_values_with_result()