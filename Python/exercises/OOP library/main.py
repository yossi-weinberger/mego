# TODO fix borrow and return methods
# TODO fix id given (without global var)

from DB import books
from book import Book
from library import Library

for i in range(3):
    book = Book()
    book.new_book()
    books.append(book)
    book.print_book()

Library.print_all_books()

Library.book_borrow()

# print(books[0].book_id)
# print(books[0].name)
# print(f"{books[0].author=}")
# print(books[0].qty)
