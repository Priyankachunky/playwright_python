import os

import pytest
from playwright.sync_api import sync_playwright

from config.settings import BASE_URL, DEFAULT_TIMEOUT, HEADLESS


@pytest.fixture(scope="session")
def playwright_fixture():
    """Fixture for Playwright instance"""
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="function")
def page():
    """Deprecated page fixture"""
    raise RuntimeError("Use the browser fixture with explicit multi-browser logic in the test.")
