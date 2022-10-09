Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with valid parameters
    Given launch chrome browser
    When open orange hrm homepage
    And Enter username "Admin" and password "admin123"
    And Click on login button
    Then User must successfully login the Dashboard page


  Scenario Outline: Login to OrangeHRM with valid parameters
    Given launch chrome browser
    When open orange hrm homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User must successfully login the Dashboard page
    Examples:
      | username | password |
      | Admin    | admin123 |
      | Onur     | a        |
      | qwerty   | qwerty   |