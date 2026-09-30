Feature: ParaBank Login
  As a ParaBank user
  I want to log in to my account
  So that I can view my account overview

  Scenario: Successful login with valid credentials
    Given the user is on the ParaBank login page
    When the user logs in with a valid username and password
    Then the Accounts Overview page should be displayed

  Scenario: Login attempt with invalid password
    Given the user is on the ParaBank login page
    When the user attempts to log in with an invalid username and password
    Then an error message should be displayed
    And the Accounts Overview page should not be displayed
