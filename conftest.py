import pytest
from playwright.sync_api import sync_playwright

BASE_URL='https://qa-practice.netlify.app/'

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) 
        context = browser.new_context(base_url=BASE_URL)
        page = context.new_page()
        yield page
        browser.close()