from playwright.async_api import Page
from playwright.sync_api import expect
from page_objects.spot_the_bugs import SpotTheBugs

def test_website_launch(browser: Page):
    browser.goto("/")
    expect(browser.get_by_text("Welcome!")).to_be_visible(timeout=10_000)

def test_without_form_details(browser: Page):
    spot_the_bugs = SpotTheBugs(browser)
    spot_the_bugs.fill_form_and_submit(
        first_name="",
        last_name="",
        phone="",
        country="",
        email="",
        password=""
    )
    
def test_with_partial_form_details(browser: Page):
    spot_the_bugs = SpotTheBugs(browser)
    spot_the_bugs.fill_form_and_submit(
        first_name="",
        last_name="",
        phone="",
        country="India",
        email="",
        password=""
    )