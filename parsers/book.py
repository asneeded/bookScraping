
import re

#import local
from locators.book_locator import BookLocator


class BookParser:

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"<Book TITLE: {self.title} PRICE: {self.price} RATING: {self.rating}>"

    @property
    def title(self):
        return self.parent.select_one(BookLocator.TITLE).attrs['title']

    @property
    def link(self):
        return self.parent.select_one(BookLocator.LINK).attrs['href']

    @property
    def price(self) -> float:
        price = self.parent.select_one(BookLocator.PRICE).string
        return float(re.search('[0-9]+\.[0-9]+', price)[0])

    @property
    def rating(self):
        rating_tag = self.parent.select_one(BookLocator.RATING)
        classes = rating_tag.attrs['class']
        rating = [rate for rate in classes if rate != 'star-rating']
        rating = BookParser.RATINGS.get(rating[0])
        return rating
