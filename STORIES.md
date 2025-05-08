"Läslistan" is a website where you can select your favorites from a catalog of books, 
or add new ones. 
The client is an organization that wants to increase reading among children and young people. 
The current version has limited functionality

User story1: Give possibility to mark a book in the website catalog as user's favorit
  As a user of service
  I want to be able to mark a book from the website catalog with a 'like'
  For be able to see this book in list of my favorit books
  
  Acceptance criteria:
    
    A1.1:
    Given I am on the book "Catalog" page
    When I click the “like” on a book
    Then the book is marked as favorite and added to my favorite list

    A1.2:
    Given a book is already marked as a favorite
    When I view that book again in the catalog
    Then the “like” icon appears in the active state

User story2: Give possibility to remove a book from a list of user favorit ones
  As a user of service
  I want to be able to remove mark 'like' for a book in the website catalog
  For be able to update list of my favorit books

  Acceptance criteria:

    A2.1:
    Given I have marked a book as favorite
    When I click the “like” icon again on that book
    Then the book is removed from my favorite list

    A2.2:
    Given the book is removed from favorites
    When I view my favorite list
    Then that book no longer appears in the list


User story3: Give possibility to see a list of user favorit books
  As a user of service
  I want to be able to see list of my favorit books
  For be able to remember what books I liked and suggest them to my friends

  Acceptance criteria:

    A3.1:
    Given I marked my favorite books with 'like' before
    When I navigate to the “Mina böcker” 
    Then I see a list of books I have marked as favorites

    A3.2:
    Given I have not marked any books with 'like' before
    When I open the “Mina böcker” page
    Then I see an empty state message “Välj dina favoriter”


User story4: Give possibility to add a new book in to the website catalog
  As a user of service
  I want to be able to add a new book in to the website catalog
  So other users of the service can get know of this book and can read it too

  Acceptance criteria:

    A4.1:
    Given I am on 'add-book' page
    When I fill out the form with book's title and author
    Then the book is added to the catalog and becomes visible to all users

    A4.2:
    Given I am on 'add-book' page
    When I try to add the book with submiting incomplete or invalid book details
    Then I see a validation error and the book is not added

