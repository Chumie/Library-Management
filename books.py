import json,os


membersFile = r"C:\TTI\Mr. Harp\Assignment 7 - Library\members.txt"
members=[]
booksFile = r"C:\TTI\Mr. Harp\Assignment 7 - Library\books.txt"
books={}
ebooksFile = r"C:\TTI\Mr. Harp\Assignment 7 - Library\ebooks.txt"
ebooks={}

def load_from_files():
    if not os.path.exists(membersFile):
        open(membersFile,'w')
    else:
        with open(membersFile, 'r') as file:
            for line in file:
                thisdict = json.loads(line)
                members.append(thisdict)

    if not os.path.exists(booksFile):
        open(booksFile,'w')
    else:
        with open(booksFile, 'r') as file:
            data = json.load(file)
            books.update(data)
            
    if not os.path.exists(ebooksFile):
        open(ebooksFile,'w')
    else:
        with open(ebooksFile, 'r') as file:
            data = json.load(file)
            ebooks.update(data)
            
class Library:
    def __init__(self, name):
        self.name = name
        self.book = {}
        self.members = []
        
    def __str__(self):
        return f"Library: {self.name}, Number of Books: {len(self.books)}, Number of Members: {len(self.members)}"

    def __repr__(self):
        return f"Library({self.name})"            
    

    def get_next_id(whicharray):
        if len(whicharray)==0:
            print("1 - ")
            return 1
        else:
            last_record = whicharray[-1]
            print("return", last_record)
            return last_record['id']+1  

    def searchBook(searchfor):
        if not books :
            return 0
        if searchfor in books:
            thisbook = books[searchfor]
            copies = input(f"The ISBN# has already {thisbook['copies']} in the books file.  Add how many copies to add? ");
            while True:
                try:
                    copies = int(copies)
                    break
                except: "You didn't enter a number.  Try again"
            
            if copies>0:
                thisbook["copies"]=thisbook["copies"]+copies
                return 1

        return 0
        
    def add_member():
        print("Add a new member to the library")
        name = input("Enter name of member: ")
        new_id = Library.get_next_id(members)
        new_member = Member(name, new_id)
        new_member = {"id": new_id, "name": name,"borrowed_books":[]}
        members.append(new_member)
                
    def add_book():
        ISBN = input("Enter ISBN: ")
        if ISBN =="":
            print("Must enter an ISBN to add a book. Cancelling...")
            return;
        isfound = Library.searchBook(ISBN)
        if isfound == 1:
            return
        title = input("Enter Book Title: ")
        author = input("Enter name of author: ")
        while True:
            copies = input('How many copies? ')
            try:
                copies = int(copies)
                break
            except ValueError:
                print("You didn't enter a number.  Try again")
            
        new_book = Book(title, author, ISBN, copies)
        books[ISBN] = {
        "title": new_book.title,
        "author": new_book.author,
        "ISBN": new_book.ISBN,
        "copies": new_book.copies
        }

        books[ISBN] = new_book

#        new_book = {"title": title, "author": author, "ISBN": ISBN, "copies":int(copies)}
#        books[ISBN] = new_book  
                
    def remove_member():
        pass
    
    def savefile():
        with open(membersFile,'w') as file:
            for member in members:
                json.dump(member,file)
                file.write('\n')

        with open(booksFile,'w') as file:
            json.dump(books, file, indent=4)
                
                
    def displayState():
        pass   
    
    def display_library_data():
        while True:
            listChoice = input("""
                1. Display Members
                2. Display Books
                X. Return to previous menu""").upper()

            if listChoice == "1":
                for member in members:
                    print(f"""
                    ID: \033[1m{member['id']:5}\033[0m | Name: \033[1m{member['name']:30}\033[0m""", end='')
                    break
                print("\n")
            if not members:
                print("There are no members yet.")   
            
            if listChoice == "2":
                for isbn, book_info in books.items():
                    print(f"""
                        ISBN: \033[1m{isbn:<6}\033[0m  |  Title: \033[1m{book_info['title']:<20}\033[0m  | Author: \033[1m{book_info['author']:<20}\033[0m  |  Copies: \033[1m{book_info['copies']}\033[0m""", end='')                   
                print("\n")
                    
            if listChoice=="X":
                return

            
class Book(Library):
    def __init__(self, title, author, ISBN, copies):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.copies = copies
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Copies: {self.copies}"
    
    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.ISBN}, {self.copies})"
    
            
class Member(Library):
    def __init__(self,name,member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = {}
        
    def __str__(self):
        return f"Name: {self.name}, Member ID: {self.member_id}, Borrowed Books: {len(self.borrowed_books)}"
    
    def __repr__(self):
        return f"Member({self.name}, {self.member_id})"

    def borrow_book(self):
        thisISBN = input(f"Welcome {self['name']}.  Enter ISBN for book you want to borrow: ")
        if thisISBN =="":
            print("You didn't enter an ISBN.  Cancelling.")
            return
        
        if thisISBN in books:
            book = books[thisISBN] 
            if book['copies']>0:
                takeout = input("{book['title']} is available.  Do you want to take it out? Y/N ").upper()
                if takeout=='Y':
                    self['borrowed_books'].append(thisISBN)
                    book['copies'] =- 1
                else:
                    input(f"{self['title']} is borrowed by another member. A Copy is not available. Press enter to continue.")
    def return_book(self):
        print(f"""
                    Welcome {self['name']}.
                    You have the following books out""")
        for book_isbn in member['borrowed_books']:
            if book_isbn in books:
                book = books[book_isbn] 
                print(f"""
                    ISBN: {book_isbn:<6} | Title: {book['title']:<20} | Author: {book['author']:<20}""", end='')
        print("\n")

        if not book:
            print("You have no borrowed books.")
        thisISBN = input(f"Enter ISBN of the book you are returning: ")
        if thisISBN in member['borrowed_books']:
            book = books[thisISBN] 
            self['borrowed_books'].remove(thisISBN)
            book['copies'] =+ 1
        else:
            print(f"You do not have ISBN# {thisISBN} out.")
            
                
    def listdata():
        for data in members:
            print(f"ID: {data['id']:5} | Name: {data['name']:30}")
            
    def remove():
        searchfor =  input("Enter the Name you want to remove: ")
        for member in members:
            thisname = member['name']
            if thisname == searchfor:
                ifsure = input("Are you sure you want to remove it? Y/N").upper()
                if ifsure=="Y":
                    members.remove(member)

class EBook(Book):
    def __init__(self, title, author, ISBN, copies, file_format):
        super().__init__(title, author, ISBN, copies)
        self.file_format = file_format

    def __str__(self):
        return f"{super().__str__()}, File Format: {self.file_format}"

    def __repr__(self):
        return f"EBook({self.title}, {self.author}, {self.ISBN}, {self.copies}, {self.file_format})"

    def add_pdf_book():
        title = input("Enter EBook Title: ")
        author = input("Enter name of author: ")
        ISBN = input("Enter ISBN: ")
        while True:
            copies = input('How many copies? ')
            try:
                copies = int(copies)
                break
            except ValueError:
                print("You didn't enter a number. Try again")
        
        new_pdf_book = EBook(title, author, ISBN, copies, "PDF")
        books[ISBN] = new_pdf_book
        print(f"PDF EBook '{title}' added with ISBN: {ISBN}")

    def add_epub_book():
        title = input("Enter EBook Title: ")
        author = input("Enter name of author: ")
        ISBN = input("Enter ISBN: ")
        while True:
            copies = input('How many copies? ')
            try:
                copies = int(copies)
                break
            except ValueError:
                print("You didn't enter a number. Try again")
        
        new_epub_book = EBook(title, author, ISBN, copies, "EPUB")
        books[ISBN] = new_epub_book
        print(f"EPUB EBook '{title}' added with ISBN: {ISBN}")
    
                    
load_from_files()

choice=" "

while choice != "X":
    print("\nLibrary Management System:")
    print("1. Member sign-in")
    print("2. Add Members")
    print("3. Add Books")
    print("4. Remove Books")
    print("5. Add Ebooks")
    print("6. Display current state of the library and members")
    print("X. Exit")

    choice = input("Enter your choice: ").upper()

    if choice == "1":
        member_id = int(input("Welcome to the Library.  Please enter your member ID: "))
        member = next((member for member in members if member.get('id') == member_id), None)
        if member is None:
            input(f"{member_id} has not been found.  Press enter to continue.")
        else:
            while True:
                memberTask = input(f"""
                        Welcome {member['name']}
                        What would you like to do?
                        1 - Borrow Book
                        2 - Return Book
                        3 - Remove Membership from Library
                        X - Exit """).upper()
                if memberTask=="1":
                    Member.borrow_book(member);
                if memberTask=="2":
                    Member.return_book(member);
                if memberTask =="3":
                    Member.remove_member(member)
                if memberTask =="X":
                    break
            
                
    elif choice == "2":
        Library.add_member()
    elif choice == "3":
        Library.add_book()
    elif choice == "4":
        pass
    elif choice == "5":
        while True:
            ebookChoice = input("""
                Ebook Menu
                1. Add PDF
                2. Add 
                                """) 
    elif choice == "6":
        Library.display_library_data()
    elif choice=="X":
        Library.savefile()
        break  
    else:
        print("Invalid choice. Please try again.")