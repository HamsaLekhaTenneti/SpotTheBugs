from playwright.async_api import Page
from playwright.sync_api import expect
from page_objects.spot_the_bugs import SpotTheBugs
from utils.set_form import set_form_valid_values

def test_check_box_validation(browser: Page):
     spot_the_bugs = SpotTheBugs(browser)
     spot_the_bugs = set_form_valid_values(spot_the_bugs)
     spot_the_bugs.navigate()
     expect(spot_the_bugs.page.locator("//input[@id='exampleCheck1']")).to_be_enabled()
     
