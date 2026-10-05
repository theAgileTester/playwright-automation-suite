Feature: Transfer Funds
  As a logged-in ParaBank user
  I want to transfer money between my own accounts
  So that I can manage my funds

  Background:
    Given the user is logged in to ParaBank
    And the user is on the Transfer Funds page

  Scenario: Successful transfer between own accounts
    When the user transfers "1" between two different accounts
    Then a "Transfer Complete!" confirmation should be displayed

  Scenario: Transfer fails when the amount is left empty
    When the user transfers "" between two different accounts
    Then a validation error about the amount should be displayed