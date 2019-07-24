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
