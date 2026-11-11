from typing import Iterator, Tuple
from uuid import uuid4

import pytest
from playwright.sync_api import Page

from config import BASE_URL, Credentials, get_credentials
from pages.login_page import LoginPage
from pages.pim_page import PimPage


@pytest.fixture
def credentials() -> Credentials:
    return get_credentials()


@pytest.fixture
def authenticated_page(page: Page, credentials: Credentials) -> Page:
    login_page = LoginPage(page)
    login_page.open(BASE_URL)
    login_page.login(credentials.username, credentials.password)
    page.wait_for_url("**/dashboard/index", wait_until="commit")
    return page


@pytest.fixture
def created_employee(authenticated_page: Page) -> Iterator[Tuple[str, str]]:
    first_name = f"Pw{uuid4().hex[:8]}"
    last_name = f"Test{uuid4().hex[:8]}"
    pim_page = PimPage(authenticated_page)
    pim_page.open_employee_list()
    pim_page.add_employee(first_name, last_name)

    yield first_name, last_name

    pim_page.open_employee_list()
    pim_page.search_employee(f"{first_name} {last_name}")
    row = pim_page.employee_row(f"{first_name} {last_name}")
    if row.count() > 0:
        pim_page.delete_employee(f"{first_name} {last_name}")
        assert row.count() == 0, "Test employee was not removed during cleanup."
