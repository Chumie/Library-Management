import json

class Book:
    def __init__(self, title, author, ISBN, copies):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.copies = copies

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Copies: {self.copies}"

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.ISBN}, {self.copies})"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"Name: {self.name}, Member ID: {self.member_id}, Borrowed Books: {len(self.borrowed_books)}"

    def __repr__(self):
        return f"Member({self.name}, {self.member_id})"

    def borrow_book(self, book):
        if book.copies > 0:
            self.borrowed_books.append(book)
            book.copies -= 1
            print(f"{self.name} has borrowed {book.title}.")
        else:
            print(f"{book.title} is currently not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.copies += 1
            print(f"{self.name} has returned {book.title}.")
        else:
            print(f"{self.name} has not borrowed {book.title}.")

class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}
        self.members = []

    def __str__(self):
        return f"Library: {self.name}, Number of Books: {len(self.books)}, Number of Members: {len(self.members)}"

    def __repr__(self):
        return f"Library({self.name})"

    def add_book(self, book):
        self.books[book.ISBN] = book

    def remove_book(self, book):
        del self.books[book.ISBN]

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        self.members.remove(member)

    def lend_book(self, member, book):
        member.borrow_book(book)

    def return_book(self, member, book):
        member.return_book(book)

class EBook(Book):
    def __init__(self, title, author, ISBN, copies, file_format):
        super().__init__(title, author, ISBN, copies)
        self.file_format = file_format

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Copies: {self.copies}, File Format: {self.file_format}"

# Scenario
library = Library("My Library")

book1 = Book("Python 101", "John Doe", "123456", 5)
book2 = Book("Java Programming", "Jane Smith", "789012", 3)
library.add_book(book1)
library.add_book(book2)

member1 = Member("Alice Smith", 1)
member2 = Member("Bob Johnson", 2)
library.add_member(member1)
library.add_member(member2)

member1.borrow_book(book1)
member2.borrow_book(book2)
member1.return_book(book1)

# Save data to JSON files
def save_data(library, filename):
    data = {
        "name": library.name,
        "books": [book.__dict__ for book in library.books.values()],
        "members": [member.__dict__ for member in library.members]
    }
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

save_data(library, "library_data.json")