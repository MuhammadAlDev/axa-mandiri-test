import re

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class AddEmployeePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.first_name: Locator = page.get_by_placeholder("First Name")
        self.last_name: Locator = page.get_by_placeholder("Last Name")
        self.save_button: Locator = page.get_by_role("button", name="Save")

    def add_employee(self, first_name: str, last_name: str) -> None:
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.save_button.click(no_wait_after=True)
        self.page.wait_for_url(
            re.compile(r".*/pim/viewPersonalDetails/empNumber/\d+"),
            wait_until="commit",
        )
