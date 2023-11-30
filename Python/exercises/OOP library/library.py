from DB import books

class Library:
    def __init__(self):
        pass

    def book_borrow():
        book_for_borrow = int(input("Type the id of the book: "))
        for i in books:
            if i.book_id == book_for_borrow:
                if i.qty > 0:
                    print("You can take the book")
                    i.qty -= 1
                else:
                    print("This book is not available")

    def book_return(self):
        book_for_return = int(input("Type the id of the book: "))
        for i in books:
            if i.book_id == book_for_return:
                print("Thank you")
                i.qty += 1

    def print_all_books():
        for book in books:
            book.print_book()
