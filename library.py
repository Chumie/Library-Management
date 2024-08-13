import json,os


membersFile = r"C:\TTI\Mr. Harp\Assignment 7 - Library\members.txt"
members=[]
booksFile = r"C:\TTI\Mr. Harp\Assignment 7 - Library\books.txt"
books=[]

def load_from_file(filename,arrayname):
    print(filename)
    if not os.path.exists(filename):
        open(filename,'w')
    else:
        with open(filename, 'r') as file:
            for line in file:
                thisdict = json.loads(line)
                arrayname.append(thisdict)

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

    def search(dataname,searchfield,searchfor):
        if not dataname :
            return 0
        for data in dataname:
            if data[searchfield] == searchfor:
                copies = int(input(f"The ISBN# has already {data['copies']} in the books file.  Add how many copies to add?"));
                if copies>0:
                    data["copies"]=data["copies"]+copies
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
        ISBN = input("Enter ISBN")
        if ISBN =="":
            print("Must enter an ISBN to add a book. Cancelling...")
            return;
        isfound = Library.search(books,"ISBN",ISBN)
        if isfound == 1:
            return
        title = input("Enter Book Title")
        author = input("Enter name of author")
        copies = int(input('How many copies?'))
        new_book = {"title": title, "author": author, "ISBN": ISBN, "copies":int(copies)}
        books.append(new_book)               
                
    def savefile():
        with open(membersFile,'w') as file:
            for member in members:
                json.dump(member,file)
                file.write('\n')

        with open(booksFile,'w') as file:
            for book in books:
                json.dump(book,file)
                file.write('\n')
                
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

    def borrow_book():
        memberId = int(input("Enter your ID# "))
        if memberId=="":
            print("Member Id cannot be empty. Cancelling ...")
            return
        thisname = ""
        for member in members:
            if member['id']==memberId:
                thisname = member['name']
                self = member
                break
        if thisname=="":
            print("Could not find this Member ID #.  Cancelling ...")
            return
        thisISBN = input(f"Welcome {thisname}.  Enter ISBN for book you want to borrow")
        if thisISBN =="":
            print("You didn't enter an ISBN.  Cancelling.")
            return
        
        bookfound=False
        for book in books:
            if book['ISBN'] == thisISBN:
                bookfound = True
                if book['copies']>0:
                    takeout = input("{book.title} is available.  Do you want to take it out? Y/N ").upper()
                    if takeout=='Y':
                        self['borrowed_books'].append(thisISBN)
                        book['copies'] =- 1
                    else:
                        input(f"{book['title']} is borrowed by another member. A Copy is not available. Press enter to continue.")
                              
        if not bookfound:
            input(f"Book with ISBN {thisISBN} is not in this library.  Press enter to continue.")
        
    def return_book():
        memberId = input("Enter your Library ID# ")
        for member in members:
            if member["id"] == int(memberId):      
                thisMember = member
                thisISBN = input(f"Welcome {member['name']}.  Enter ISBN of the book you are returning")
                
    def listdata():
        for data in members:
            print(f"ID: {data['id']:5} | Name: {data['name']:30}")
            
    def remove():
        searchfor =  input("Enter the Name you want to remove")
        for member in members:
            thisname = member['name']
            if thisname == searchfor:
                ifsure = input("Are you sure you want to remove it? Y/N").upper()
                if ifsure=="Y":
                    members.remove(member)
            
load_from_file(membersFile,members) 
load_from_file(booksFile,books)

choice=" "
while choice.upper() != "X":    
    choice = input("""Library Management System
    MENU
    1 - Add Member
    2 - Add Book
    3 - Remove Book
    4 - Borrow Book
    5 - Return Book
    6 - View Members
    7 - Remove Member
    X - Exit""")

    if choice=="1":
        Library.add_member();
    if choice=="2":
        Book.add_book();
    if choice=="4":
        Member.borrow_book();
    if choice=="5":
        Member.return_book();
    if choice=="6":
        Member.listdata()
    if choice=="7":
        Member.remove()
    if choice.upper()=="X":
        Library.savefile()       