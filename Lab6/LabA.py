#Name: Ethan Carrera
#Date: 9/6/2021
#Lab A
#---------------------------------------
#Variable Dictionary
#
#
#
#
#
#
#----------------------------------------


import csv

#total uh individuals??
total = 0

#last name
lName = []

#first naem
fName = []

#birthday
bday = []

print("{0}\t{1}\t{2}\t{3}\n".format("Index","Last Name","First Name","Date of Birth"))

#connecting to the csv file!

with open ("/Classes/SE126/Lab6/CSV/lab6A.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        total += 1

        ln = rec[0]
        fn = rec[1]
        bd = rec[2]

        lName.append(ln)
        fName.append(fn)
        bday.append(bd)

for i in range(0,total):
    print("{0:2}\t{1:18}{2:15}{3:9}".format(i, lName[i], fName[i],bday[i]))
        
#keepign the while loop as a yes
answer = "y"

bi_count = 0

while answer =="y":
    
    search = input("\nWho is it you're looking for? Please enter their last name.\nEnter: ")

    min = 0

    max = total - 1

    guess = int((min+max) / 2)

    #increasing order

    while(min<max and search != lName[guess]):
        bi_count += 1

        if search < lName[guess]:
            max = guess - 1
        
        else:
            min = guess + 1
        
        guess = int((min + max) / 2)

    if search == lName[guess]:
        #if found

        print("{0} was found at index {1}" .format(search,guess))

        print("\nLAST NAME: {0}  |  FIRST NAME: {1}  |  BIRTHDAY {2}".format(lName[guess], fName[guess], bday[guess]))

    else: 
        print("Your search for {0} was NOT FOUND".format(search))

        print("\nName might be mispeled please try again!")
    
    print("SEARCH LOOP:{0}".format(bi_count))

    bi_count = 0 #restart the count

    answer = input("Do you want to enter another name?\n[y/n]: ")

    while answer != 'y' and answer != 'n':
        print("ERROR")
        answer = input("Do you want to enter another name?\n[y/n]: ")

print("Thank you for using this application. Have a beautiful day! ByeBye!")