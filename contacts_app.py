'''
@Author: Sidharath Khanna
@StudentId: C0901950
@Date: 23/10/2023
@Program: To design and implement a simple, Personal Contacts Application for managing personal contacts, utilizing Python's dictionaries and lists.
'''

# ContactDetails as a Dictionary
contactDetails = {"name" : "" , "phone" : "", "email" : "", "address" : ""}

# Contact List as a list of dictionary 
contactList = [{"name" : "sid" , "phone" : 2496881750, "email" : "sid@gmail.com", "address" : "Scarborough"},
               {"name" : "khanna" , "phone" : 9872662341, "email" : "khanna@gmail.com", "address" : "Toronto"},
               {"name" : "dis" , "phone" : 123456789, "email" : "dis@gmail.com", "address" : "North York"}
            ]

# defining Menu function
def menu():
    print("-------------------------------")
    print(" Personal Contacts Application ")
    print("-------------------------------")
    print(" 1. View All Contacts")
    print(" 2. Add A New Contact")
    print(" 3. Search A Contact")
    print(" 4. Update A Contact")
    print(" 5. Delete A Contact")
    print(" 6. Exit App")
    print("-------------------------")
    return input("Enter your choice: ")


# defining find function to find name in our Contact List, i.e. list of contactDetails, which is list of dictionary.
def find(name):
    # flag
    found = False 
    for contact in contactList:
        if contact["name"] == name:
            found = True
            break
        else:
            found = False
    if found:
        return contact
    else:
        return 0


# defining viewContacts function 
def viewContacts():
    # If list is empty, or you delete all entries
    if len(contactList) == 0:
        print('\n'"You have NO cotacts in your contacts list!")
    else:
        print('\n'"You have following cotacts in your contacts list: ")
        
        for contact in contactList:
            # print([contact.get("name"), contact.get("phone"), contact.get("email"), contact.get("address")])  # Simple list of contacts with details
            print(f' Name: {contact.get("name")} \n Phone: {str(contact.get("phone"))} \n Email: {contact.get("email")} \n Address: {contact.get("address")}')  # preferred readable format
            print()      
        '''
        # Code with enumerate(), to add 'id' attribute while displaying the contacts, because dictionary doesn't have indexes.
        for num, contact in enumerate(contactList, start=1):
            print(f"Contact {num}:")
            for key, value in contact.items():
                print(f"{key.capitalize()}: {value}")
            print()
        '''


# defining addContacts function 
def addContacts():
    name = input("Please enter the name you want to add: ")
    # Checking if contact doesn't exist already  
    if find(name) == 0:
        # Try Catch Block for catching the run time error, of user giving an alphanumeric number.
        try:
            phone = int(input("Please enter mobile number [Numerical]: "))
        except ValueError:
            # If there's an error in mobile number, its been reset to 0, and user is asked to update is using option 4.
            # This saves us from getting a run-time-error.
            print("Oops! That's not a valid number. Proceeding with 0 as the default value.")
            phone = 0
            print("You can update the phone details afterwards by choosing option 4")
        email = input("Please enter email id: ")
        address = input("Please enter address: ")
        contactList.append(dict([("name", name), ("phone", phone), ("email", email), ("address", address)]))
        print(f" {name}'s detials successfully added to your contact list!!")
    else:
        print(f" {name}'s details already exists in your contact list!!")
        print(" Please choose option 1 to view all your contacts!")


# defining searchContacts function 
def searchContacts():
    name = input("Please enter the name you want to search: ")
    contact = find(name)
    # If contact found, show details 
    if contact != 0:
            print(f" {name}'s details found in your contacts!!")
            print("Please find below the contact's details: ")
            # print(f' Name: {contact.get("name")} \n Phone: {str(contact.get("phone"))} \n Email: {contact.get("email")} \n Address: {contact.get("address")}')  # readable format
            # Another way of prnting key value pair in python dictionary.
            for key, value in contact.items():
                print(f" {key.capitalize()}: {value}") 
    else:
        print(f" {name}'s details not found in your contacts!!")
        print(" Please choose option 2 to add it!")


# defining updateContacts function 
def updateContacts():
    name = input("Please enter the name of the contact you want to update: ")
    contact = find(name)
    # If contact not found  
    if contact == 0:
        print(f" {name}'s details doesn't exists in your contact list!!")
        print(" Please choose option 1 to view all your contacts!")
    else:
        detail = input(f"Please enter the detail you'd like to update for '{name}' [name/phone/email/address]: ")
        value = input("Please enter the new value: ")
        contact[detail] = value
        print(f" Your '{detail}' for '{name}' is updated!!")
        print(f" New value for {name}'s {detail} is {value}!")
        

# defining deleteContacts function 
def deleteContacts():
    name = input("Please enter the name you want to delete from your contact list: ")
    contact = find(name)
    # If contact not found  
    if contact == 0:
        print(f" {name}'s details doesn't exists in your contact list!!")
        print(" Please choose option 1 to view all your contacts!")
    else:
        contactList.remove(contact)
        print(f" {name}'s detials successfully deleted from your contact list!!")


# defining main function 
def main():
    while True:
        # calling menu method
        case = menu()
        if case == "1":
            # calling viewContacts method
            viewContacts()
        elif case == "2":
            # calling addContacts method
            addContacts()
        elif case == "3":
            # calling searchContacts method
            searchContacts()
        elif case == "4":
            # calling updateContacts method
            updateContacts()
        elif case == "5":
            # calling deleteContacts method
            deleteContacts() 
        elif case == "6":
            # An exit option
            print("Thanks for checking in!! Goodbye!")
            break
        else:
            # Bad input
            print("Wrong Input!! please select a valid option!!")


# Calling main function 
main()