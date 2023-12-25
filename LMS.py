# @Author: Sidharath Khanna
# @StudentId: C0901950
# @Date: 03/10/2023

# defining menu function
def menu():
    print("-------------------------")
    print("Library Management System")
    print("-------------------------")
    print("1. Display All Books")
    print("2. Add Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")
    print("-------------------------")
    return input("Enter your choice: ")


# defining displayAllBooks function
def displayAllBooks():
    # for book in open("library_db.txt"):
    #     print(book.strip('\n'))

    # Opening the file in reading mode.
    bookList = open("library_db.txt", "r")
    books = bookList.readlines()
    print("Please find the list of books here:")
    for book in books:
        print(book.strip('\n'))
    bookList.close()


# defining addBooks function
def addBooks():
    newBookTitle = input("Please enter the Name of Book: ")
    newBookAuthor = input("Please enter the Author of Book: ")
    found = False

    # Opening the file in reading mode.
    bookList = open("library_db.txt", 'r')
    books = bookList.readlines()
    count = len(books)
    # Opening the file in Appending mode.
    updatedList = open('library_db.txt', 'a')

    for book in books:
        bookInfo = (book.strip('\n').split(","))
        if bookInfo[1].strip().strip('"').lower() == newBookTitle.lower() and bookInfo[2].strip().strip('"').lower() == newBookAuthor.lower():
            found = True
            print("We can not add the book because its already there in the library!")
            break
        else:
            found = False

    if not found:
        # Adding the book to the list and Updating its availability.
        updatedList.write(f"{count + 1}, \"{newBookTitle}\", \"{newBookAuthor}\", Yes\n")
        print("Congratulations!! Your book was added to the library!")

    # Closing the file in reading and Writing mode.
    bookList.close()
    updatedList.close()


# defining borrowBooks function
def borrowBooks():
    # Asking user for the input for the book to be borrowed.
    borrowBookTitle = input("Please enter the Name of Book: ")
    found = False

    # Opening the file in reading mode.
    bookList = open('library_db.txt', 'r')
    books = bookList.readlines()

    # Opening the file in writing mode.
    updatedList = open('library_db.txt', 'w')

    for book in books:
        bookInfo = book.strip('\n').split(",")
        # print(bookInfo[1].replace('"', '').strip().lower())
        if bookInfo[1].strip().strip('"').lower() == borrowBookTitle.lower():
            if bookInfo[3].strip() == "Yes":
                # Updating the list with book availability.
                updatedList.write(f"{bookInfo[0].strip()}, {bookInfo[1].strip()}, {bookInfo[2].strip()}, No\n")
                print(f"You borrowed the Book {bookInfo[1].strip()} successfully!")
            else:
                print("The book you are trying to borrow is not available at the moment!")
                print("Please try again later!!")
                updatedList.write(book)
            found = True
        else:
            updatedList.write(book)

    if not found:
        print("Sorry, the book is not in the library.")

    # Closing the file in reading and writing mode.
    bookList.close()
    updatedList.close()


# defining returnBooks function
def returnBooks():
    # Asking user for the input for the book to be returned
    # bookReturn = input("Enter the Book you want to return: ") # Searching with book name
    bookReturn = input("Enter the ID for the Book you want to return: ")
    found = False

    # Opening the file in reading mode.
    bookList = open('library_db.txt', 'r')
    books = bookList.readlines()

    # Opening the file in writing mode.
    updatedList = open('library_db.txt', 'w')

    for book in books:
        bookInfo = book.strip('\n').split(",")
        # if bookInfo[1].strip().strip('"').lower() == bookReturn.lower():  # Searching with book name
        if bookInfo[0].strip() == bookReturn:
            # print(f"book name {bookInfo[1]} found")   # Debugging
            if bookInfo[3].strip() == "No":
                # Updating the file with book availability.
                updatedList.write(f"{bookInfo[0].strip()}, {bookInfo[1].strip()}, {bookInfo[2].strip()}, Yes\n")
                print(f"Book number {bookInfo[0].strip()}, {bookInfo[1].strip()} returned successfully!")
            else:
                print("This book is already available in the library.")
                updatedList.write(book)
            found = True
        else:
            updatedList.write(book)

    if not found:
        print("Sorry! book not found.")

    # Closing the file in reading and writing mode.
    bookList.close()
    updatedList.close()


# defining searchBooks function
def searchBooks():
    search = input("Please enter the Name of the Book/Author you want to search: ")
    found = False
    result = []

    # Opening the file in reading mode.
    bookList = open('library_db.txt', 'r')
    books = bookList.readlines()

    for book in books:
        bookInfo = book.strip('\n').split(",")
        # Searching the book with the Book / Author name
        if bookInfo[1].strip().strip('"').lower() == search.lower() or bookInfo[2].strip().strip('"').lower() == search.lower():
            found = True
            result.append(book)
        else:
            continue

    if found:
        print("Please find below the list of books based upon your search:")
        for b in result:
            print(b.strip('\n'))
    else:
        print("Sorry! No books were found corresponding to the name you searched for!")
        print("Kindly select option 1 from menu for displaying all books in our library!")

    # Closing the file in reading mode.
    bookList.close()


# defining main function
def main():
    while True:
        choice = menu()
        if choice == '1':
            # Calling displayAllBooks function
            displayAllBooks()
        elif choice == '2':
            # Calling addBooks function
            addBooks()
        elif choice == '3':
            # Calling borrowBooks function
            borrowBooks()
        elif choice == '4':
            # Calling returnBooks function
            returnBooks()
        elif choice == '5':
            # Calling searchBooks function
            searchBooks()
        elif choice == '6':
            print("Thanks for checking in! Goodbye!")
            break
        else:
            print("Bad Input!! Please choose a valid option!")


# Calling main function
main()
