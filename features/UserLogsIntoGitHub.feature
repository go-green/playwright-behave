Feature: User login scenarios

  Scenario: User is able to login to GitHub using valid credentials
    Given I have navigated to GitHub login page
    When I enter my valid credentials
    Then I am navigated to the default landing page