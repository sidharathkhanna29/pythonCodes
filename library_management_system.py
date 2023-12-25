'''
@Author: Sidharath Khanna
@StudentId: C0901950
@Date: 07/11/2023
@Program: To design a program that encapsulates the details of books and the operations of a library system. The system will handle different categories of books without using inheritance.
'''

# Class Book
class Book:
    # defining __init__ function 
    def __init__(self, title, author, isbn, available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = available
    
    # defining checkout function 
    def checkout(self):
        if self.availability:
            self.availability = False
            return f"{self.title} from Books has been checked out."
        else:
            return f"{self.title} from Books is already checked out."

    # defining return_book function 
    def return_book(self):
        if not self.availability:
            self.availability = True
            return f"{self.title} from Books has been returned."
        else:
            return f"{self.title} from Books is already available."
    
    # defining __str__ function     
    def  __str__(self):
        return (f'Book Title : {self.title},\n Book Author: {self.author},\n Book ISBN Number: {self.isbn},\n Book Available: {"Yes" if self.availability else "No"}')

# a = Book("sid", "khanna", 1232, False)
# print(f'a : {a} ')

# Class FictionBook
class FictionBook:
    # defining __init__ function 
    def __init__(self, title, author, isbn, available, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = available
        self.genre = genre
    
    # defining checkout function 
    def checkout(self):
        if self.availability:
            self.availability = False
            return f"{self.title} from Fiction Books has been checked out."
        else:
            return f"{self.title} from Fiction Books is already checked out."

    # defining return_book function 
    def return_book(self):
        if not self.availability:
            self.availability = True
            return f"{self.title} from Fiction Books has been returned."
        else:
            return f"{self.title} from Fiction Books is already available."
    
    # defining __str__ function     
    def  __str__(self):
        return (f'Book Title : {self.title},\n Book Author: {self.author},\n Book ISBN Number: {self.isbn},\n Book Available: {"Yes" if self.availability else "No"},\n Genre: {self.genre} ')

# b = FictionBook("sid", "khanna", 1232, False, "Sci-Fi")
# print(f'b : {b} ')


# Class NonFictionBook
class NonFictionBook:
    # defining __init__ function 
    def __init__(self, title, author, isbn, available, field):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = available
        self.field = field
    
    # defining checkout function 
    def checkout(self):
        if self.availability:
            self.availability = False
            return f"{self.title} from Non Fiction Books has been checked out."
        else:
            return f"{self.title} from Non Fiction Books is already checked out."

    # defining return_book function 
    def return_book(self):
        if not self.availability:
            self.availability = True
            return f"{self.title} from Non Fiction Books has been returned."
        else:
            return f"{self.title} from Non Fiction Books is already available."
    
    # defining __str__ function     
    def  __str__(self):
        return (f'Book Title : {self.title},\n Book Author: {self.author},\n Book ISBN Number: {self.isbn},\n Book Available: {"Yes" if self.availability else "No"},\n Field: {self.field} ')

# c = NonFictionBook("sid", "khanna", 1232, False, "MEMOIR")
# print(f'c : {c} ')

# Class Library
class Library:
    # defining __init__ function 
    def __init__(self):
        self.book_catalog = []
        self.fiction_catalog = []
        self.non_fiction_catalog = []

    # defining add_book function 
    def add_book(self, type, title, author, isbn, genre, field):
        if type.lower() == "book":
            book = Book(title, author, isbn, True)
            self.book_catalog.append(book)
        elif type.lower() == "fiction":
            fbook = FictionBook(title, author, isbn, True, genre)
            self.fiction_catalog.append(fbook)
        elif type.lower() == "non fiction":
            nfbook = NonFictionBook(title, author, isbn, True, field)
            self.non_fiction_catalog.append(nfbook)
        else:
            print("Sorry! Couldn't add your book, as Type of the book is incorrect!")

    # defining list_books function 
    def list_books(self):
        print("\nBooks in Book Catalog:")
        print("------------------------")
        if len(self.book_catalog) == 0:
            print("No Books")
        else:
            for book in self.book_catalog:
                print(book, "\n")

        print("\nBooks in Fiction Catalog:")
        print("---------------------------")        
        if len(self.fiction_catalog) == 0:
            print("No Books")
        else:
            for book in self.fiction_catalog:
                print(book, "\n")

        print("\nBooks in Non-Fiction Catalog:")
        print("-------------------------------")
        if len(self.non_fiction_catalog) == 0:
            print("No Books")
        else:
            for book in self.non_fiction_catalog:
                print(book, "\n")

    # defining checkout_book function 
    def checkout_book(self, title, type):
        if type.lower() == "book":
            for book in self.book_catalog:
                if book.title.lower() == title.lower():
                    print(book.checkout())
                    break
            else:
                print(f"Sorry!, the book {title} is not available!!")                    
        
        elif type.lower() == "fiction":
            for fbook in self.fiction_catalog:
                if fbook.title.lower() == title.lower():
                    print(fbook.checkout())
                    break
            else:
                print(f"Sorry!, the book {title} is not available!!")
        
        elif type.lower() == "non fiction":
            for nfbook in self.non_fiction_catalog:
                if nfbook.title.lower() == title.lower():
                    print(nfbook.checkout())
                    break
            else:
                print(f"Sorry!, the book {title} is not available!!")
        
        else:
            print("Please Enter the correct Type of the book")

    # defining return_book function 
    def return_book(self, title, type):
        if type.lower() == "book":
            for book in self.book_catalog:
                if book.title.lower() == title.lower():
                    print(book.return_book())
                    break
            else:
                print(f"Sorry!, the book {title} is not available!!")
                    
        elif type.lower() == "fiction":
            for fbook in self.fiction_catalog:
                if fbook.title.lower() == title.lower():
                    print(fbook.return_book())
                    break
            else:
                print(f"Sorry!, the book {title} is not available!!")

        elif type.lower() == "non fiction":
            for nfbook in self.non_fiction_catalog:
                if nfbook.title.lower() == title.lower():
                    print(nfbook.return_book())
                    break
            else:
                print(f"Sorry!, the book {title} is not available!!")
        
        else:
            print("Please Enter the correct Type of the book")

    # defining check_availability function 
    def check_availability(self, title, type):
        if type.lower() == "book":
            for book in self.book_catalog:
                if book.title.lower() == title.lower() and book.availability:
                    print(f"Yes, the book {title} is available!!")
                    break
            else:
                print(f"Sorry!, the book {title} is not available!!")
                    
        elif type.lower() == "fiction":
            for fbook in self.fiction_catalog:
                if fbook.title.lower() == title.lower() and fbook.availability:
                    print(f"Yes, the book {title} is available!!")
                    break
            else:
                print(f"Sorry!, the book {title} is not available!!")

        elif type.lower() == "non fiction":
            for nfbook in self.non_fiction_catalog:
                if nfbook.title.lower() == title.lower() and nfbook.availability:
                    print(f"Yes, the book {title} is available!!")
                    break
            else:
                print(f"Sorry!, the book {title} is not available!!")
            
        else:
            print("Please Enter the correct Type of the book")


# defining menu function
def menu():
    print("----------------------------------------------")
    print("Welcome to Lambton Library Management System!!")
    print("----------------------------------------------")
    print(" 1. Add A New Book")
    print(" 2. List All Books")
    print(" 3. Checkout A Book")
    print(" 4. Return A Book")
    print(" 5. Check Book Availability")
    print(" 6. Exit App")
    print("-------------------------")
    return input("Please enter your choice: ")


# defining main function 
def main():
    library = Library()
    
    # Hard coded some Book names for Testing purposes, can be added through program as well
    library.add_book("Book", "Python", "John", "1234567890", "Tech", "Python" )
    library.add_book("Book", "Adventure", "Alice", "9876543210", "Sci-fi", "")
    library.add_book("Book", "Sid", "Bob", "5678901234", "Biography", "")
    library.add_book("Non Fiction", "Python", "Smith", "5678901234", "", "Programming")
    
    while True:
        # calling menu method
        case = menu()

        if case == "1":
            type = input("Please enter the Type of the book: (Book / Fiction / Non Fiction): ")
            title = input("Please enter the Name of the book you want to add: ")
            author = input("Please enter the Author of the book: ")
            isbn = input("Please enter the ISBN number of the book: ")
            genre = input("Please enter the Genre of the book: ")
            field = input("Please enter the Field of the book: ")
            # calling add_book method
            library.add_book(type, title, author, isbn, genre, field)
        
        elif case == "2":
            # calling list_books method
            library.list_books()
        
        elif case == "3":
            title = input("Please enter the Name of the book you want to checkout: ")
            type = input("Please enter the type of the book: (Book / Fiction / Non Fiction): ")
            # calling checkout_book method
            library.checkout_book(title, type)
        
        elif case == "4":
            title = input("Please enter the Name of the book you want to return: ")
            type = input("Please enter the type of the book: (Book / Fiction / Non Fiction): ")
            # calling return_book method
            library.return_book(title, type)
        
        elif case == "5":
            # checking if book is available
            title = input("Please enter the Name of the book you want to check : ")
            type = input("Please enter the type of the book: (Book / Fiction / Non Fiction): ")
            # calling check_availability method
            library.check_availability(title, type)
        
        elif case == "6":
            # An exit option
            print("Thanks for checking in!! Goodbye!")
            break
        
        else:
            # Bad input
            print("Wrong Input!! please select a valid option!!")
    

# Calling main function 
main()