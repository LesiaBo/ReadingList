def book_in_catalog_with_title(page, title):
    return page.get_by_test_id(f'star-{title}')

def book_in_catalog(page, title):
    return page.locator("div.book", has_text=f"{title}")

def click_on_catalog_link(page):
    page.get_by_test_id('catalog').click(timeout=100)

