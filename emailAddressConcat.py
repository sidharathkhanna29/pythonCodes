#Author: Sidharath Khanna C950 CSD_1133_5
#Date: November 17, 2023
#Version: 1.0.0.0
#Variables used: I, Count, FirstName, LastName, Email
#Program name: A program that allows the user to input a list of first names into one array and last names into a parallel array. Input should be terminated when the user enters a sentinel character. The output should be a list of email addresses where the address is of the following form: first.last@mycollege.edu

#Initialize Variables
I = 0
Max = 100
FirstName  = [""] * Max
LastName = [""] * Max
Email = [""] * Max

# Do While Loop with Sentinel value as a string "done"
while True:
	FirstName[I] = input(f"Please Enter the First Name of student number {I + 1} OR Enter 'done' to finish: ")		# User Input
	if (FirstName[I].lower() == "done"):
		break
	LastName[I] = input(f"Please Enter the Last Name of student number {I + 1} OR Enter 'done' to finish: ")		# User Input
	if (LastName[I].lower() == "done"):
		break
	else:
		Email[I] = 	FirstName[I] + "." + LastName[I] + "@mycollege.edu"		# Concatinating Email Addresses
		I += 1  															# Incrementing Counter
#Printing Output
print("\n List of Email ids:")
if Email[0] == "":
		print("\t Sorry there are no email id's present in the list")
else:
    for I in range(len(Email)):
        if Email[I]:
            print(f"\t Email Id for Student {I + 1} is: {Email[I]}")