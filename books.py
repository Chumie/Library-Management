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
    
    def addbook(self):
        pass
 
    def get_next_id(whicharray):
        if len(whicharray)==0:
            print("1 - ")
            return 1
        else:
            last_record = whicharray[-1]
            print("return", last_record)
            return last_record['id']+1
    


    def search():
        input("Enter ID# or search by name")
        open(membersFile,'r')

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
        self.borrowed_books = []
        
    def __str__(self):
        return f"Name: {self.name}, Member ID: {self.member_id}, Borrowed Books: {len(self.borrowed_books)}"
    
    def __repr__(self):
        return f"Member({self.name}, {self.member_id})"

    def add_member(self,name,member_id):
        new_member = {"id":member_id, "name": name}
        members.append(new_member)

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

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
    choice = input("""Library Management System\n\nMENU\n1 - Add Member\n2 - Add Book\n3 - Remove Book\n4 - Borrow Book\n5 - Return book\n6 - View Members\n7.Remove Member\nX Exit""")
    if choice=="1":
        print("Add a new member to the library")
        name = input("Enter name of member: ")
        new_id = Library.get_next_id(members)
        new_member = Member(name, new_id)
        new_member.add_member(name,new_id)
    if choice=="6":
        Member.listdata()
    if choice=="7":
        Member.remove()
    if choice.upper()=="X":
        Library.savefile()
        