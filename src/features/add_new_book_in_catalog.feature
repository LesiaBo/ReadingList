Feature:
  User story4: Give possibility to add a new book in to the website catalog

Background:
    Given I'm on a "Läslistan" webpage

  Scenario: A4.1. Add a new book into the website catalog
    When I go to page "Lägg till book"
    And I type text "Pippi Långstrump" into the text filed 'Titel'
    And I type text "Astrid Lindgren" into the text filed 'Författare'
    Then Button 'Lägg till ny book' is active
    And I click on the button 'Lägg till ny book'
    Then Button 'Lägg till ny book' is inactive
    When I go to 'Katalog' page
    Then Book with name "Pippi Långstrump" and author "Astrid Lindgren" should be shown at the page

  Scenario Outline: A4.2.1, A4.2.2. Trying to add book without giving title
    When I go to page "Lägg till book"
    And I type text "<title>" into the text filed 'Titel'
    And I type text "<author>" into the text filed 'Författare'
    Then Button 'Lägg till ny book' is inactive
    When I go to 'Katalog' page
    Then Book with title "<text_should_not_find>" isn't shown in the website catalog
    Examples:
    | title    | author                             | text_should_not_find               |
    | Mamma Mu | ""                                 | Mamma Mu                           |
    | ""       | Jujja Wieslander, Tomas Wieslander | Jujja Wieslander, Tomas Wieslander |

