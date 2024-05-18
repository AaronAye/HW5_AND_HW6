Feature: Test Scenarios for Target Search

  Scenario: Verify Target search results
    Given Open Target main page
    When Verify target circle HW_5
    When Search for item Coffee HW_5
    When Click on add to cart HW_5
    Then Verify item in cart HW_5
