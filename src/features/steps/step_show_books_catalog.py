
from behave import when, then, given
from playwright.sync_api import expect

@given(u'I\'m on a "Läslistan" webpage')
def step_on_main_page(context):
    context.page.goto(context.base_url)

@when(u'I go to \'Katalog\' page')
def step_go_to_page_katalog(context):
    context.page.get_by_test_id('catalog').click(timeout=10000)

@then(u'Book with name "{title}" and author "{author}" should be shown at the page')
def step_book_data_is_in_the_list(context,title,author):
    book = context.page.get_by_test_id(f'star-{title}')
    expect(book).to_be_visible(timeout=1000)

@then(u'Book with title "{title}" isn\'t shown in the website catalog')
def step_book_data_is_not_in_the_list(context, title):
    assert context.page.locator("div.book", has_text=f"{title}").count() == 0


