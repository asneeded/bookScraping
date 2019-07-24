import requests
from pages.books_page import BookPage

page_content = requests.get('http://books.toscrape.com/').content

page = BookPage(page_content)

books = page.books

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
    loop = True
    while loop:
        menu()


if __name__ == '__main__':
    main()
