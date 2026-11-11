import re
from typing import Tuple

from playwright.sync_api import Page, expect

from config import BASE_URL, Credentials
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.pim_page import PimPage


def test_login_with_valid_credentials_opens_dashboard(
    page: Page, credentials: Credentials
) -> None:
    login_page = LoginPage(page)
    login_page.open(BASE_URL)
    login_page.login(credentials.username, credentials.password)

    page.wait_for_url("**/dashboard/index", wait_until="commit")
    expect(DashboardPage(page).dashboard_label).to_be_visible()


def test_login_with_invalid_credentials_shows_error(
    page: Page, credentials: Credentials
) -> None:
    login_page = LoginPage(page)
    login_page.open(BASE_URL)
    login_page.login(credentials.username, f"{credentials.password}-invalid")

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(
        re.compile(r"Invalid Credentials", re.IGNORECASE)
    )


def test_pim_employee_list_opens_with_empty_search_fields(
    authenticated_page: Page,
) -> None:
    pim_page = PimPage(authenticated_page)
    pim_page.open_employee_list()

    expect(pim_page.employee_list_label).to_be_visible()
    expect(pim_page.employee_list_tab).to_be_visible()
    assert pim_page.search_fields_are_empty()


def test_search_employee_shows_matching_table_row(
    authenticated_page: Page, created_employee: Tuple[str, str]
) -> None:
    first_name, last_name = created_employee
    pim_page = PimPage(authenticated_page)
    pim_page.open_employee_list()
    pim_page.search_employee(f"{first_name} {last_name}")

    row = pim_page.employee_row(f"{first_name} {last_name}")
    expect(row).to_have_count(1)
    expect(row.get_by_text(first_name, exact=True)).to_be_visible()
    expect(row.get_by_text(last_name, exact=True)).to_be_visible()


def test_delete_employee_removes_it_from_table(
    authenticated_page: Page, created_employee: Tuple[str, str]
) -> None:
    first_name, last_name = created_employee
    full_name = f"{first_name} {last_name}"
    pim_page = PimPage(authenticated_page)
    pim_page.open_employee_list()
    pim_page.search_employee(full_name)

    row = pim_page.employee_row(full_name)
    expect(row).to_have_count(1)
    pim_page.delete_employee(full_name)
    expect(row).to_have_count(0)
