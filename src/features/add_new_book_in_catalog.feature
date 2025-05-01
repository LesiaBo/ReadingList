Feature:
  Give possibility to add a new book in to the website catalog

Background:
    Given I'm on a "Läslistan" webpage

  Scenario: Add a new book into the website catalog
    When I go to page "Lägg till book"
    And I type text "Pippi Långstrump" into the text filed 'Titel'
    And I type text "Astrid Lindgren" into the text filed 'Författare'
    Then Button 'Lägg till ny book' is active
    And I click on the button 'Lägg till ny book'
    Then Button 'Lägg till ny book' is inactive
    When I go to 'Katalog' page
    Then Book with name "Pippi Långstrump" and author "Astrid Lindgren" should be shown at the page

  Scenario: Trying to add book without giving title
    When I go to page "Lägg till book"
    And I type text "Mamma Mu" into the text filed 'Titel'
    And I'm leaving field 'Författare' empty
    Then Button 'Lägg till ny book' is inactive
    When I go to 'Katalog' page
    Then Book with title "Mamma Mu" isn't shown in the website catalog

  Scenario: Trying to add book without giving author
    When I go to page "Lägg till book"
    And I'm leaving field 'Title' empty
    And I type text "Jujja Wieslander, Tomas Wieslander" into the text filed 'Författare'
    Then Button 'Lägg till ny book' is inactive
    When I go to 'Katalog' page
    Then Book with title "Jujja Wieslander, Tomas Wieslander" isn't shown in the website catalog
