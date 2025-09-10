Feature: Create Account page
    A page where the user can create an account.

    Scenario Outline: Creating an Account
        Given I am on the sign-up page
        When I enter "<username>" into the username field
        And I enter "<password>" into the password field
        And I click the "Create Account" button
        Then I should be redicted to the 'Verify Account' page
        And I should see a success message

        Examples:
            | username          | password          |
            | myaccount123      | p@ssw0rd789       |
            | new-user          | v€ry$ecuRe88      |
            | temp.acc          | 6n0onekN0w$       |