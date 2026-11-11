from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate(self, url: str) -> None:
        self.page.goto(url, wait_until="domcontentloaded")

    def title(self) -> str:
        return self.page.title()
