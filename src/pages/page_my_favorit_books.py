def click_on_my_books_link(page):
    page.get_by_test_id('favorites').click(timeout=100)

def my_favorit_book_with_title(page, title):
    return page.get_by_test_id(f'fav-{title}')

def no_books_in_list_of_favorits_message(page):
    return page.get_by_text("När du valt, kommer dina favoritböcker att visas här")
