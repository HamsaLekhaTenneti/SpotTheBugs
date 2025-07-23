from playwright.async_api import Page
from playwright.sync_api import expect
from page_objects.spot_the_bugs import SpotTheBugs
from utils.set_form import set_form_valid_values

def test_first_name_label(browser: Page):
    """
    Email should always have @ and domain
    """
    spot_the_bugs = SpotTheBugs(browser)
    spot_the_bugs.navigate()

    expect(spot_the_bugs.page.locator('label[for="firstName"]')).to_have_text("First Name")
    expect(spot_the_bugs.page.locator('label[for="lastName"]').nth(0)).to_have_text("Last Name*")
    expect(spot_the_bugs.page.locator('label[for="phoneNumber"]').nth(1)).to_have_text("Phone number*")
    expect(spot_the_bugs.page.locator('label[for="exampleInputEmail1"]')).to_have_text("Email address*")