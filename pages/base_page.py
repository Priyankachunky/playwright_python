"""
Base Page Object for all pages
"""
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.default_timeout = 30000

    def navigate(self, url: str):
        """Navigate to URL"""
        self.page.goto(url)

    def wait_for_load_state(self):
        """Wait for page to load"""
        self.page.wait_for_load_state('networkidle')

    def wait_for_selector(self, selector: str, timeout: int = None):
        """Wait for selector to be visible"""
        self.page.wait_for_selector(selector, timeout=timeout or self.default_timeout)

    def click(self, selector: str):
        """Click on element"""
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        """Fill input field"""
        self.page.fill(selector, text)

    def is_visible(self, selector: str) -> bool:
        """Check if element is visible"""
        return self.page.is_visible(selector)

    def get_text(self, selector: str) -> str:
        """Get text from element"""
        return self.page.text_content(selector)

    def select_option(self, selector: str, value: str):
        """Select option from dropdown"""
        self.page.select_option(selector, value)

    def check(self, selector: str):
        """Check checkbox"""
        self.page.check(selector)

    def is_checked(self, selector: str) -> bool:
        """Check if checkbox is checked"""
        return self.page.is_checked(selector)

    def get_title(self) -> str:
        """Get page title"""
        return self.page.title()
