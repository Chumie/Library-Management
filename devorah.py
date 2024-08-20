import json,os

membersFile = r"C:\TTI\Mr. Harp\Assignment 7 - Library\members.txt"
members=[]
booksFile = r"C:\TTI\Mr. Harp\Assignment 7 - Library\books.txt"
books=[]

def add_book():
    #ISBN is the book_id  BUT !!! if it is in sql, then will it allow me to put it in ?  change it? 
    # book_id = Book.get_next_id(books) # invoking the get_next_id def as inherited function from Library
    title = input("Enter Book Title: ")
    author = input("Enter the name of the author of this book")
    ISBN = input("Enter the ISBN of this book")
    copies = input("How many copies of this book are you adding?")
    new_book  = Book(title, author, ISBN, copies)  #  this creates an instance of the book class with the inputted data inside
    books.append(new_book)
    print(books)
        
def get_next_id(whicharray):
    if len(whicharray) == 0:
        return 1
    else:
        last_record = whicharray[-1]
        return last_record['id'] + 1     

def load_from_file(filename,arrayname):  # this gets the files(passed parameters) into arrays for use in program 
    if not os.path.exists(filename):
        open(filename,'w')
    else:
        with open(filename, 'r') as file:
            for line in file:
                thisdict = json.loads(line)
                if arrayname=="member":
                    members.append(thisdict)
                else:
                    books.append(thisdict)     
                             
def savefile():  #this function puts both the members list and the books list into the files and saves them
    with open(membersFile,'w') as file:
        for member in members:
            json.dump(members,file)
            file.write('\n')   
                    
    with open(booksFile,'w') as file:
        for book in books:
            json.dump(books,file)
            file.write('\n')
                    
def add_member(name):
    member_id=get_next_id(members)
    new_member = {"id":member_id, "name": name}
    members.append(new_member)
    print("hello")       
def remove_Member():
    searchfor = input ("Enter Name you want to remove")
    for member in members : 
        thisname=member['name']
        if thisname == searchfor:
            ifsure = input("are you sure you want to remove this? y/n").upper()
            if ifsure == 'Y':
                members.remove(member)   
                            
def list_members(members):
    for member in members: 
        pass
        #print(f'id={member['id']} name = {member['name']}\n')                             

class Library:
    def __init__(self, name):
        self.name = name
        self.book = {}
        self.members = []
        
    def __str__(self):
        return f"Library: {self.name}, Number of Books: {len(self.books)}, Number of Members: {len(self.members)}"

    def __repr__(self):
        return f"Library({self.name})"            
    
    def addbook(self):
        pass
 
    def search():
        input("Enter ID# or search by name")
        open(membersFile,'r')
                
class Book():
    def __init__(self, title, author, ISBN, copies):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.copies = copies
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Copies: {self.copies}"
    
    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.ISBN}, {self.copies})"
    
class Member():
    def __init__(self,name,member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        
    def __str__(self):
        return f"Name: {self.name}, Member ID: {self.member_id}, Borrowed Books: {len(self.borrowed_books)}"
    
    def __repr__(self):
        return f"Member({self.name}, {self.member_id})"

 

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

load_from_file(membersFile,"members")   # invokes function to get member data into list to use in program
load_from_file(booksFile,"books")       # invokes function to get book  data into list to use in program
while True :  
 #   choice = input("""Library Management System\n\nMENU\n1 - Add Member\n2 - Add Book\n3 - Remove Book\n4 - Borrow Book\n5 - Return book\n6 - View Members\n7 Delete Member\nX - Quit  """)
    print("\nLibrary Management System")
    print(" 1. Add Member")
    print(" 2. Update Member")
    print(" 3. Remove Member")
    print(" 4. Add book ")
    print(" 5. Update Book")
    print(" 6. Remove Book")
    print(" 7. Borrow Book")
    print(" 8. Return Book")
    print(" 9. Display Members")
    print("10. Display Books")
    print("11. Exit") 
    choice = input("Enter your choice: ")
    # menu should be add member, borrow book, return book, add book to library, add another copy of an existing book to the library, remove 1 copy of a book from library, delete member, view members (and books they borrowed), view books  
    if choice == "11":
        savefile()  # saves lists (both member and books) to txt file -- will change when doing postman
        break # leave program
    if choice=="1":
        print("Add a new member to the library")
        name = input("Enter name of member: ")
        add_member(name) # this runs add_member function on the instance, and sends the parameters to add 
    if choice == '2': 
       update_Member()
    if choice == '3': 
       remove_Member()
    if choice=="4":
        # print("Add a new Book to the library")
        # new_book = Book("t",'t','0',0)
        add_book() # this runs add_book function on the class and sends the parameters to add 
    if choice == '5': 
       update_Book()
    if choice == '6': 
       remove_Book()
    if choice == '7': 
       remove_Book()
    if choice == '8': 
       remove_Book()
    if choice == "9":
        list_members(members)
    if choice == "10":
        list_books(books)
    