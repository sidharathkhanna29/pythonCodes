"""
Date : 2023-10-03
# loops application
# Files : Its most common way of storing data on secondary storage.
# Data ----> stored in RAM ---> hold on to data for later use
# Two general type of files when it comes to any programming languages
1 ) TXT FILES (String) ---> it let you store your input/ output
great for individual single datas
*** to store each entry into each line of text
2) DATA FILES (binary files) ---> great for complex data (data structure)
# list, tuples, dictionaries, objects from classes, ...
# you need to convert data to binary (Serialization)
-------------------------------------------------------------
# 1) you have to open file ( you create a file object which link
your file to your script -
*** in some languages the file may not existed so you have to create a
file two
# 2) Set the mode write (w), read (r) , append (a)
# 3) process
# 4) close file (why we have to close the files?)
# *** your information may not be saved
# each file can be utilized by one application at the time!
"""

def writeInfoToFile():
    afile = open('demo.txt', 'w') # open/create a file
    afile.write('Hesam\n')
    afile.write('Tony\n')
    afile.write('Alex\n')
    afile.write(str(3)+'\n')
    afile.close()

def appendInfoToFile():
    afile = open('demo.txt', 'a')
    afile.write("PYTHON\n")
    afile.close()

#appendInfoToFile()
#writeInfoToFile()

def readAFile():
    afile = open('demo.txt')  # default mode is read
    # 1) in form of string!
    print('tell --->', afile.tell())
    output = afile.read() # reads the whole file and return a string!
    print(output) # quick glimpse of the file
    print('tell --->', afile.tell())
    afile.seek(0) # reset the cursor
    print('tell --->', afile.tell())
    alist = afile.readlines() # read all the lines, return a list from the file
    print(alist) #
    len(alist)
    for line in alist :
        print(line.strip('\n'))
    afile.seek(0) # move the cursor to the beginning.
    print('--------------------------------------------')
    aline = afile.readline() # reads the first line
    while aline != '':
        print(aline.strip('\n'))
        aline = afile.readline() # reads the first line


#readAFile()

for line in open('demo.txt'):
    print(line.strip('\n'))

# ---------------------------------- break (30 minutes)------------


a = 'ABCDABCA'
print(a.lstrip('A'))
print(a.rstrip('A'))
print(a.strip('A'))

# -------------- application to help the user record sales figures--------
def menu():
    print('1 - Record sales on a new Sales file ')
    print('2 - add sales to an existing Sales file')
    print('3 - Display sales file, total and average sales')
    print('4 - Exit')
    return input('Enter 1,2,3, or 4 : ')
import os
def recordSalesNewFile():
    file_name = input('Enter a file name : ') + ".txt"
    if not os.path.exists(file_name):
        afile = open(file_name, 'w')
        n_sales = input(f'Enter the number of sales for file {file_name}')
        if not n_sales.isdigit():
            print('Bad input! digit must be entered! ')
            print('start over!')
            return
        n_sales = int(n_sales)
        i = 0
        while i < n_sales:
            a = input(f'Enter the sales # {i+1}:')
            if a.isdigit():
                afile.write(a +'\n')
                i += 1
            else:
                print('Your sales has to be a digit! EX: 23')

        afile.close()
        print(f'the sales recorded  on {file_name}')
    else:
        print('file is exist! use menu 2 to update')
    # note that this file should not exist!
def addSalesExisting():
    file_name = input('Enter a file name : ') + ".txt"
    if os.path.exists(file_name):
        afile = open(file_name, 'a')
        n_sales = input(f'Enter the number of sales for file {file_name}')
        if not n_sales.isdigit():
            print('Bad input! digit must be entered! ')
            print('start over!')
            return
        n_sales = int(n_sales)
        i = 0
        while i < n_sales:
            a = input(f'Enter the sales # {i+1}:')
            if a.isdigit():
                afile.write(a +'\n')
                i += 1
            else:
                print('Your sales has to be a digit! EX: 23')

        afile.close()
    else:
        print('file is NOT exist! use menu 1 to record the new sale')
def displaySales():
    print('Enter one of the following : ')
    list_files_in_directory(os.getcwd())

    file_name = input('Enter a file name : ') + ".txt"
    if os.path.exists(file_name):
        count = 0
        add = 0
        for line in open(file_name):
            line = line.strip('\n')
            if line.isdigit():
                print(f' $ {float(line):.2f} ')
                count += 1
                add += float(line)
        print(f'Total sale is $ {add:.2f}')
        print(f'The avg sales: $ {add/count:.2f}')


    else:
        print('file is not exists!')


def main():
    while True:
        choice = menu()
        if choice == '1': recordSalesNewFile()
        elif choice == '2' : addSalesExisting()
        elif choice == '3': displaySales()
        elif choice == '4': break
        else: print('Bad input!')


def list_files_in_directory(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                if '.txt' in entry.name:
                    print(entry.name)

main()