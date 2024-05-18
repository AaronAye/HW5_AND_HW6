Feature: Test Scenarios for Target Search

  Scenario: Verify Target search results
    Given Open Target main page
    When Search for SkinnyPop
    Then Verify search results has SkinnyPop
