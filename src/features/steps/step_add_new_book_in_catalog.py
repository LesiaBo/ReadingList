import time
from playwright.sync_api import expect
from behave import when, then, given
from src.pages.page_add_new_book_in_catalog import (fill_books_title, fill_books_author,
                                                    laag_till_ny_book_button,click_on_add_link)

@when(u'I go to page "Lägg till book"')
def step_go_to_page_lagg_till_book(context):
    click_on_add_link(context.page)

@when(u'I type text "{title}" into the text filed \'Titel\'')
def step_when_i_type_books_title(context, title):
    if title == '""':
        title = ''
    fill_books_title(context.page, title)

@when(u'I type text "{author}" into the text filed \'Författare\'')
def step_when_i_type_books_author(context, author):
    if author == '""':
        author = ''
    fill_books_author(context.page, author)

@then(u'I click on the button \'Lägg till ny book\'')
@when(u'I click on the button \'Lägg till ny book\'')
def step_click_add_button(context):
    laag_till_ny_book_button(context.page).click(force=True, timeout=10000)

@then(u'Button \'Lägg till ny book\' is inactive')
def step_button_add_is_inactive(context):
    assert laag_till_ny_book_button(context.page).is_disabled()

@then(u'Button \'Lägg till ny book\' is active')
def step_button_add_is_active(context):
    assert laag_till_ny_book_button(context.page).is_enabled()

@when(u'I\'m leaving field \'Title\' empty')
def step_field_title_is_empty(context):
    fill_books_title(context.page, "")

@when(u'I\'m leaving field \'Författare\' empty')
def step_field_author_is_empty(context):
    fill_books_author(context.page, "")
