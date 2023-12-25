# defining menu function
def menu():
    print("-------------------------")
    print("Library Management System")
    print("-------------------------")
    print("1. Display All Books")
    print("2. Add Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")
    print("-------------------------")
    return input("Enter your choice: ")


# defining displayAllBooks function
def displayAllBooks():
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

    bookList = open("library_db.txt", 'r')
    books = bookList.readlines()
    count = len(books)
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
        updatedList.write(f"{count + 1}, \"{newBookTitle}\", \"{newBookAuthor}\", Yes\n")
        print("Congratulations!! Your book was added to the library!")


    bookList.close()
    updatedList.close()

# defining Books function
def borrowBooks():
    borrowBookTitle = input("Please enter the Name of Book: ")
    found = False

    bookList = open('library_db.txt', 'r')
    books = bookList.readlines()

    updatedList = open('library_db.txt', 'w')

    for book in books:
        bookInfo = book.strip('\n').split(",")
        if bookInfo[1].strip().strip('"').lower() == borrowBookTitle.lower():
            if bookInfo[3].strip() == "Yes":
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

    bookList.close()
    updatedList.close()


# defining returnBooks function
def returnBooks():
    bookReturn = input("Enter the ID for the Book you want to return: ")
    found = False

    bookList = open('library_db.txt', 'r')
    books = bookList.readlines()

    updatedList = open('library_db.txt', 'w')

    for book in books:
        bookInfo = book.strip('\n').split(",")
        if bookInfo[0].strip() == bookReturn:
            if bookInfo[3].strip() == "No":
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

    bookList.close()
    updatedList.close()


# defining main function
def main():
    while True:
        choice = menu()
        if choice == '1':
            displayAllBooks()
        elif choice == '2':
            addBooks()
        elif choice == '3':
            borrowBooks()
        elif choice == '4':
            returnBooks()
        elif choice == '5':
            print("Thanks for checking in!")
            break
        else:
            print("Bad Input!! Please choose a valid option!")

# Calling main function
main()
