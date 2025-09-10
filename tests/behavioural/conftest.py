import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    """Provides a Playwright browser instance for the entire test session."""
    with sync_playwright() as p:
        # Launch the browser in headless mode (no UI)
        browser = p.chromium.launch(headless=True)
        yield browser
        # Close the browser instance after all tests are done
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    """Provides a new browser page for each test function."""
    page = browser.new_page()
    yield page
    # Close the page after the test function has run
    page.close()

@pytest.fixture
def user_data():
    """Provides a simple dictionary of test user data."""
    return {
        "username": "testuser",
        "password": "password123",
        "email": "test@example.com"
    }