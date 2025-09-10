from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import sync_playwright

from ..conftest import page

@scenarios('../../../features/app/create_account.feature')

@given("I am on the sign-up page")
def navigate_to_signup(page):
    page.goto("localhost:3000")

@when(parsers.parse('I want to create an account with the username {username}'))
def enter_username(page, username):
    page.fill("#username-input", username)

@when(parsers.parse('I enter {password} into the password field'))
def enter_password(page, password):
    page.fill("#password-input", password)

@when(parsers.parse('I click the "Create Account" button'))
def click_create_account(page):
    page.click("#create-account-btn")

@then("I should be redicted to the 'Verify Account' page")
def redirected_to_verify_account(page):
    assert "verify" in page.url

@then("I should see a success message")
def verify_success_message(page):
    assert page.text_content("#success-message") == "Account created successfully!"