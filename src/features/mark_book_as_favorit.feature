Feature:
  Give possibility to mark a book from the website catalog as favorit

Background:
    Given I'm on a "Läslistan" webpage

  Scenario: Add a book as my favorit and then remove it from there
    When I mark book "Min katt är min chef" from the website catalog with a 'like'
    Then The book "Min katt är min chef" gets a 'heart' mark
    When I mark book "Jag trodde det var tisdag" from the website catalog with a 'like'
    Then The book "Jag trodde det var tisdag" gets a 'heart' mark
    When I'm removing 'like' from book "Jag trodde det var tisdag"
    Then The book "Jag trodde det var tisdag" doesn't have a 'heart' mark
    When I go to 'Mina böker' page
    Then I able to see the book "Min katt är min chef" is in list of my favorit books
    And I able to see the book "Jag trodde det var tisdag" is NOT in list of my favorit books