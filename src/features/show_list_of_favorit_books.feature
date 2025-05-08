Feature:
  User story3: Give possibility to see a list of user favorit books

Background:
    Given I'm on a "Läslistan" webpage

  Scenario: A3.1. Mark a book as a favorit and find it in the list of favorits
    When I mark book "Kaffekokaren som visste för mycket" from the website catalog with a 'like'
    Then The book "Kaffekokaren som visste för mycket" gets a 'heart' mark
    When I go to 'Mina böcker' page
    Then I able to see the book "Kaffekokaren som visste för mycket" is in list of my favorit books

  Scenario: A3.2. Validate that the list of favorit books is empty when no books is marked with a 'like'
    Given I have not marked any books with 'like' before
    When I go to 'Mina böcker' page
    Then I see an empty state message “Välj dina favoriter”