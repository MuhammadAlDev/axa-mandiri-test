from playwright.sync_api import Page

from pages.example_page import ExamplePage


def test_page_title_and_heading(page: Page) -> None:
    page.set_content("<title>Example page</title><h1>Hello, Playwright!</h1>")
    example_page = ExamplePage(page)

    assert example_page.title() == "Example page"
    assert example_page.heading_is_visible()
