import pytest
import time
import subprocess
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session", autouse=True)
def start_server():
    """Starts and stops the application server for the test session."""
    print("Starting server...")
    process = subprocess.Popen(
        ["uv", "run", "python", "main.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Wait for the server to be ready
    time.sleep(5)
    print("Server started.")

    # 'yield' hands control to the tests.
    yield process

    # Teardown: Stop the server after all tests have completed
    print("Stopping server...")
    process.terminate()
    process.wait()  # Wait for the process to exit
    print("Server stopped.")

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