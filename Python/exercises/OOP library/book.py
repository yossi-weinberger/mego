id_for_books = 1

class Book:
    def __init__(self):
        #global id_for_books
        self.book_id = 0
        self.name = ""
        self.author = ""
        self.qty = 1

    def new_book(self):
        global id_for_books
        self.book_id = id_for_books
        self.name = input("Type the name of the book: ")
        self.author = input("Type the name of the author: ")
        self.qty = int(input("Type the QTY of the copies: "))
        #global id_for_books
        id_for_books += 1


    def print_book(self):
        print("\n-------")
        print(f"ID: {self.book_id}")
        print(f"Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Quantity: {self.qty}\n")