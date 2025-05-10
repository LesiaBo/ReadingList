import time, re

from playwright.sync_api import expect
from behave import when, then, given
from src.pages.page_books_catalog import (book_in_catalog_with_title)

@when(u'I mark book "{title}" from the website catalog with a \'like\'')
@when(u'I\'m removing \'like\' from book "{title}"')
def step_mark_book_as_favorit(context, title):
    book_in_catalog_with_title(context.page, title).click(timeout=1000)
    time.sleep(5)

@given(u'I have not marked any books with \'like\' before')
def step_dont_mark_any_book_with_like(context):
    print("I didn't find any book I like yet")

@then(u'The book "{title}" gets a \'heart\' mark')
def step_check_if_book_is_marked_as_favorit(context, title):
    book = book_in_catalog_with_title(context.page, title)
    expect(book).to_have_class(re.compile(r'\bstar\b.*\bselected\b'))

@then(u'The book "{title}" doesn\'t have a \'heart\' mark')
def step_check_if_book_is_not_marked_as_favorit(context, title):
    book = book_in_catalog_with_title(context.page, title)
    expect(book).not_to_have_class(re.compile(r'\bstar\b.*\bselected\b'))
    expect(book).to_have_class(re.compile(r'\bstar'))


