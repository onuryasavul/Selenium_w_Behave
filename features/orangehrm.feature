Feature: OrangeHRM Logo
  Scenario: Logo presence on OrangeHRM home page
    Given launch chrome browser
    When open orange hrm homepage
    Then verify that the logo is present on the page
    And close browser
