import re

from playwright.sync_api import Locator, Page

from pages.add_employee_page import AddEmployeePage
from pages.base_page import BasePage


class PimPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.pim_menu: Locator = page.get_by_role("link", name="PIM")
        self.employee_list_label: Locator = page.get_by_text(
            "Employee Information", exact=True
        )
        self.employee_list_tab: Locator = page.get_by_text(
            "Employee List", exact=True
        ).first
        self.employee_name_input: Locator = page.get_by_placeholder(
            "Type for hints..."
        ).first
        self.search_button: Locator = page.get_by_role("button", name="Search")
        self.add_employee_link: Locator = page.get_by_role(
            "link", name="Add Employee"
        )

    def open_employee_list(self) -> None:
        self.pim_menu.click(no_wait_after=True)
        self.page.wait_for_url(
            re.compile(r".*/pim/viewEmployeeList(?:\?.*)?$"),
            wait_until="commit",
        )
        self.employee_list_label.wait_for()

    def is_employee_list_loaded(self) -> bool:
        return (
            self.page.url.endswith("/pim/viewEmployeeList")
            and self.employee_list_label.is_visible()
        )

    def search_fields_are_empty(self) -> bool:
        return self.page.locator(".oxd-form input").evaluate_all(
            "inputs => inputs.length > 0 && inputs.every(input => input.value === '')"
        )

    def add_employee(self, first_name: str, last_name: str) -> None:
        self.add_employee_link.click()
        AddEmployeePage(self.page).add_employee(first_name, last_name)

    def search_employee(self, full_name: str) -> None:
        self.employee_name_input.fill(full_name)
        self.page.locator(".oxd-autocomplete-option").filter(
            has_text=full_name
        ).first.click()
        self.search_button.click()
        self.page.locator(".oxd-table-body").wait_for()

    def employee_row(self, full_name: str) -> Locator:
        return self.page.locator(".oxd-table-card").filter(has_text=full_name)

    def delete_employee(self, full_name: str) -> None:
        row = self.employee_row(full_name)
        row.locator("button").first.click()
        self.page.get_by_role("button", name=re.compile(r"Yes,\s*Delete", re.I)).click()
        row.wait_for(state="detached")
