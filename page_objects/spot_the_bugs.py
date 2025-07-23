from playwright.async_api import Page

class SpotTheBugs:

    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("/bugs-form")

    def fill_form_and_submit(
            self,
            first_name,
            last_name,
            phone,
            country,
            email,
            password
        ):
        self.navigate()
        self.page.locator("//input[@id='firstName']").fill(first_name)
        self.page.locator("//input[@id='lastName']").fill(last_name)
        self.page.locator("#phone").fill(phone)
        self.page.locator("//select[@id='countries_dropdown_menu']").select_option(country)
        self.page.locator("//input[@id='emailAddress']").fill(email)
        self.page.locator("#password").fill(password)
        self.page.wait_for_timeout(2000)

        self.page.locator("//button[@id='registerBtn']").click()


