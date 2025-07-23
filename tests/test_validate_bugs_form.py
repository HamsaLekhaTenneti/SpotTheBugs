from playwright.async_api import Page
from page_objects.spot_the_bugs import SpotTheBugs

# Always first set valid values
def set_form_valid_values(spot_the_bugs: SpotTheBugs):
    """
    This is to set valid values
    """
    spot_the_bugs.set_form_values(
        first_name="Sample First Name",
        last_name="Sample Last Name",
        phone="098877889900",
        country="India",
        email="dcsdfsf@cdsv.com",
        password="asdasfefhuweh"
    )
    return spot_the_bugs


def test_with_valid_form_details(browser: Page):
    """
    This is to validate form details when all the values are written correctly
    """
    spot_the_bugs = SpotTheBugs(browser)
    spot_the_bugs.set_form_values(
        first_name="Sample First Name",
        last_name="Sample Last Name",
        phone="098877889900",
        country="India",
        email="dcsdfsf@cdsv.com",
        password="asdasfefhuweh"
    )
    spot_the_bugs.fill_form()
    spot_the_bugs.submit_form()
    spot_the_bugs.validate_success_message()
    spot_the_bugs.validate_values_with_result()


def test_with_invalid_email(browser: Page):
    spot_the_bugs = SpotTheBugs(browser)

    # With Invalid email
    spot_the_bugs = set_form_valid_values(spot_the_bugs)
    spot_the_bugs.email = "ggsggg"
    spot_the_bugs.fill_form()
    spot_the_bugs.submit_form()
    spot_the_bugs.validate_invalid_details()


def test_with_invalid_phone(browser: Page):
    spot_the_bugs = SpotTheBugs(browser)

    spot_the_bugs = set_form_valid_values(spot_the_bugs)
    spot_the_bugs.phone = "ggahkhdgghshjjj"
    spot_the_bugs.fill_form()
    spot_the_bugs.submit_form()
    spot_the_bugs.validate_invalid_details()