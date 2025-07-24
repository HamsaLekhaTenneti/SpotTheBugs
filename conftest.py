import pytest
from playwright.sync_api import sync_playwright

BASE_URL='https://qa-practice.netlify.app/'

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        # When running from local machine --
        # browser = p.chromium.launch(headless=False)
        browser = p.chromium.launch() 
        context = browser.new_context(base_url=BASE_URL)
        page = context.new_page()
        yield page
        browser.close()