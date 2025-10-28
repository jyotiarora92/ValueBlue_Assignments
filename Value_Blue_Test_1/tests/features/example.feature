Feature: Example

  Scenario: FinishMe
    Given I start the browser
    When I navigate to "http://example.com"
    And I click on the "More information..." link
    Then A link with text "RFC 2606" must be present
    And A link with text "RFC 6761" must be present
    And the 'Domain Names' box must contain "Root Zone Management" at index 2
