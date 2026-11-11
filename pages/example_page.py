from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class ExamplePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.heading: Locator = page.get_by_role("heading", name="Hello, Playwright!")

    def heading_is_visible(self) -> bool:
        return self.heading.is_visible()
