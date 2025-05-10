import time

def click_on_add_link(page):
    page.get_by_test_id('add-book').click(timeout=1000)

def fill_books_title(page, title):
    page.get_by_test_id('add-input-title').click(timeout=1000)
    page.get_by_test_id('add-input-title').fill(title)

def fill_books_author(page, author):
    page.get_by_test_id('add-input-author').click(timeout=1000)
    page.get_by_test_id('add-input-author').fill(author)

def laag_till_ny_book_button(page):
    return page.get_by_test_id('add-submit')


