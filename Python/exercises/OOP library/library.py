from DB import books
from book import Book


class Library:
    def __init__(self):
        pass

    def book_borrow():
        self.id = int(input("Type the id of the book: "))
        if self.qty > 0:
            print("You can take the book")
            self.qty -= 1
        else:
            print("This book is not available")

    def book_return(self):
        print("Thank you")
        self.qty += 1

    def print_all_books():
        for book in books:
            book.print_book()
