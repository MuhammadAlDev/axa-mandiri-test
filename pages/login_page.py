import re

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.username: Locator = page.get_by_placeholder("Username")
        self.password: Locator = page.get_by_placeholder("Password")
        self.login_button: Locator = page.get_by_role("button", name="Login")
        self.error_message: Locator = page.get_by_text(
            re.compile(r"Invalid Credentials", re.IGNORECASE)
        )

    def open(self, url: str) -> None:
        self.navigate(url)

    def login(self, username: str, password: str) -> None:
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click(no_wait_after=True)

    def has_invalid_credentials_error(self) -> bool:
        return self.error_message.is_visible()
