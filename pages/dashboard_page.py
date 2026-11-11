from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.dashboard_label: Locator = page.get_by_text("Dashboard", exact=True).first

    def is_loaded(self) -> bool:
        return self.dashboard_label.is_visible()
