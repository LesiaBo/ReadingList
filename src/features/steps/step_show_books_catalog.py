
from behave import when, then, given
from playwright.sync_api import expect
from src.pages.page_books_catalog import (book_in_catalog_with_title, click_on_catalog_link, book_in_catalog)

@given(u'I\'m on a "Läslistan" webpage')
def step_on_main_page(context):
    context.page.goto(context.base_url)

@when(u'I go to \'Katalog\' page')
def step_go_to_page_katalog(context):
    click_on_catalog_link(context.page)

@then(u'Book with name "{title}" and author "{author}" should be shown at the page')
def step_book_data_is_in_the_list(context,title,author):
    book = book_in_catalog_with_title(context.page, title)
    expect(book).to_be_visible(timeout=100)

@then(u'Book with title "{title}" isn\'t shown in the website catalog')
def step_book_data_is_not_in_the_list(context, title):
    assert book_in_catalog(context.page, title).count() == 0


