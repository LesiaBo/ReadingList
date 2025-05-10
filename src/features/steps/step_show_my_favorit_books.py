from behave import when, then, given
from playwright.sync_api import expect
import time
from src.pages.page_my_favorit_books import (click_on_my_books_link, my_favorit_book_with_title,
                                             no_books_in_list_of_favorits_message)


@when(u'I go to \'Mina böcker\' page')
def step_go_to_page_my_books(context):
    click_on_my_books_link(context.page)
    time.sleep(5)

@then(u'I able to see the book "{title}" is in list of my favorit books')
def step_check_that_book_is_in_my_favorits_list(context, title):
    book = my_favorit_book_with_title(context.page, title)
    expect(book).to_be_visible(timeout=100)

@then(u'I able to see the book "{title}" is NOT in list of my favorit books')
def step_check_that_book_is_not_in_my_favorits_list(context, title):
    book = my_favorit_book_with_title(context.page, title)
    expect(book).not_to_be_visible(timeout=100)

@then(u'I see an empty state message “Välj dina favoriter”')
def step_check_no_favorits_message(context):
    message = no_books_in_list_of_favorits_message(context.page)
    expect(message).to_be_visible(timeout=100)

