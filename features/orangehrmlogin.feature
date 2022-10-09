Feature: OrangeHRM Login
  Scenario: Login to OrangeHRM with valid parameters
    Given launch browser
    When open orangehrm homepage
    And Enter username "Admin" and password "admin123"
    And Click on login button
    Then User must successfully login the Dashboard page
