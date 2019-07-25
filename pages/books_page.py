import re
from bs4 import BeautifulSoup

# Local Imports
from locators.all_books_locator import AllBooksPageLocator
from parsers.book import BookParser


class BookPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        locator = AllBooksPageLocator.BOOKS
        book_tag = self.soup.select(locator)
        return [BookParser(e) for e in book_tag]

    @property
    def page_count(self):
        content = self.soup.select_one(AllBooksPageLocator.PAGER).string
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        return int(matcher.group(1))
