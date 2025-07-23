from playwright.async_api import Page
from playwright.sync_api import expect

class SpotTheBugs:

    def __init__(self, page: Page):
        self.page = page
        self.first_name = ""
        self.last_name = ""
        self.phone = 0
        self.email = ""
        self.country = ""
        self.password = ""

    def set_form_values(
            self,
            first_name,
            last_name,
            phone,
            country,
            email,
            password
        ):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.country = country
        self.email = email
        self.password = password

    def navigate(self):
        self.page.goto("/bugs-form")

    def fill_form(self):
        self.navigate()
        self.page.locator("//input[@id='firstName']").fill(self.first_name)
        self.page.locator("//input[@id='lastName']").fill(self.last_name)
        self.page.locator("#phone").fill(self.phone)
        self.page.locator("//select[@id='countries_dropdown_menu']").select_option(self.country)
        self.page.locator("//input[@id='emailAddress']").fill(self.email)
        self.page.locator("#password").fill(self.password)

    def submit_form(self):
        self.page.locator("//button[@id='registerBtn']").click()

    def fill_and_submit(self):
        self.fill_form()
        self.submit_form()

    def validate_values_with_result(self):
        """
        Method to validate the success register comparisons
        """
        expect(self.page.get_by_text(f"First Name: {self.first_name}")).to_be_visible()
        expect(self.page.get_by_text(f"Last Name: {self.last_name}")).to_be_visible()
        expect(self.page.get_by_text(f"Phone Number: {self.phone}")).to_be_visible()
        expect(self.page.get_by_text(f"Country: {self.country}")).to_be_visible()
        expect(self.page.get_by_text(f"Email: {self.email}")).to_be_visible()

    def validate_success_message(self):
        """
        Method to validate if success message is displayed
        """
        expect(self.page.get_by_text("Successfully registered the following information")).to_be_visible()        
        
    def validate_invalid_details(self):
        """
        Method to validate if success not displayed when some information is wrongly written
        """
        expect(self.page.get_by_text("Successfully registered the following information")).not_to_be_visible()
    