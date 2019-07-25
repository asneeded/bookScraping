import requests
import logging
from pages.books_page import BookPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='logs.txt')

logger = logging.getLogger('scraping')


logger.info('Loading books list...')

page_content = requests.get('http://books.toscrape.com/').content
page = BookPage(page_content)

books = page.books

for i in range(1, page.page_count):
    url = f"http://books.toscrape.com/catalogue/page-{i+1}.html"
    page_content = requests.get(url).content
    page = BookPage(page_content)
    books.extend(page.books)


# page = BookPage(page_content)


# all_books = [BookPage(requests.get(pages).content) for pages in all_page]

# for p in page.books:
#     print(p)


def menu():
    user_input = input('''
    Welcome to all the books:
    Search Menu
    [1] - Stars
    [2] - Price
    [3] - All
    [q] - Quit
    ''')
    while user_input != 'q':
        if user_input == '1':
            print(search_star())
        elif user_input == '2':
            pass
        elif user_input == '3':
            pass
        elif user_input.lower == 'q':
            pass


def search_star():
    star_input = input('What star rating? ')
    return [b for b in page.books if b.rating >= int(star_input)]


def main():
    menu()


if __name__ == '__main__':
    main()
