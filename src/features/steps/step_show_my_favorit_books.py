from behave import when, then, given
from playwright.sync_api import expect
import time


@when(u'I go to \'Mina böker\' page')
def step_go_to_page_my_books(context):
    context.page.get_by_test_id('favorites').click(timeout=10000)
    time.sleep(10)


@then(u'I able to see the book "{title}" is in list of my favorit books')
def step_check_that_book_is_in_my_favorits_list(context, title):
    book = context.page.get_by_test_id(f'fav-{title}')
    expect(book).to_be_visible(timeout=1000)


@then(u'I able to see the book "{title}" is NOT in list of my favorit books')
def step_check_that_book_is_not_in_my_favorits_list(context, title):
    book = context.page.get_by_test_id(f'fav-{title}')
    expect(book).not_to_be_visible(timeout=1000)


