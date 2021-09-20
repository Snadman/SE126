#Name: Ethan Carrera
#Date: 9/15/2021
#Lab: A
#Variable Dictionary:



#---------------------------------------------

#-------------------------------------------

#----Main Code--------------------------------

import csv

#Canvas
from os import system, name 
from time import sleep 


def clear():   
     if name == 'nt':
        _ = system('cls')  
   

#do last name before first (shown on canvas)
id = []
lName = []
fName = []
age = []
alg = []


with open ("Lab7/text/GOT_bubble_sort_7.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file: 

        id.append(rec[0])
        lName.append(rec[1])
        fName.append(rec[2])
        age.append(int(rec[3]))
        alg.append(rec[4])


#print menu
def menu(): 

    print("\nWelcome to the Menu bar, Please select one of the following ")
    
    print("\n1: Search by FIRST NAME")
    
    print("\n2: Search by ID CODE")
    
    print("\n3: Search by LAST NAME")
    
    print("\n4: Search by ALLEGIANCE")
    
    print("\n5: Exit Program")
    choice = int(input("Please Select a number: "))

    while choice < 1 or choice > 5:
        print()
        print("INVALID NUMBER")
        print()
        choice = int(input("Please Select a number: "))

    return choice

#asks the user if they want to try or go again
def again():

    answer = input("Would you like to go again? [y/n] ")
    answer = answer.lower()

    return answer


#switching
def switch(listName, position):

    temp = listName[position]
    listName[position] = listName[position + 1]
    listName[position + 1] = temp


men = menu()

answer = "y"


while answer == "y":

    for i in range(0, len(fName) - 1):

        for a in range(0, len(fName) - 1):

            if fName[a] > fName[a + 1]:

                switch(fName, a)
                switch(lName, a)
                switch(age, a)
                switch(id, a)
                
            

    if men == 1:

        print()
        search = input("Please enter in the first name you are looking for ")

        min = 0
        max = len(fName) - 1
        guess = int((min + max) / 2)

        while (min < max and search != fName[guess]):

            if search < fName[guess]:

                max = guess - 1

            else:
                min = guess + 1

            guess = int((min + max) / 2)

        if search == fName[guess]:
            print() 
            print("Person was Located!!")
            print("\n{0:13}\t  {1:9}\t  {2:9}\t  {3:2}\t  {4:30}".format("ID CODE", "LAST NAME", "FIRST NAME", "AGE", "ALLEGIANCE"))
            print() 
            print("{0:13}\t  {1:9}\t  {2:9}\t  {3:2}\t  {4:30}".format(id[guess], lName[guess], fName[guess], age[guess], alg[guess]))


        else:
            print("{0} was not found. Please try again ".format(search))


        twice = again()

        if twice == "y":

            men = 1

        else:

            input("Press enter to go back to menu")
            men = menu()



    for i in range(0, len(id) - 1): 

        for k in range(0, len(id) - 1):

            if id[k] > id[k + 1]:

                switch(fName, k)
                switch(id, k)
                switch(age, k)
                switch(id, k)

    


    if men == 2:

        print() 
        search = input("Please enter in the id code you are looking for: ")

        min = 0
        max = len(id) - 1
        guess = int((min + max) / 2)

        while (min < max and search != id[guess]):

            if search < id[guess]:

                max = guess - 1

            else:
                min = guess + 1

            guess = int((min + max) / 2)

        if search == id[guess]:
            print("\nID Code Located")

            print("\n{0:13}\t  {1:9}\t  {2:9}\t  {3:2}\t  {4:33}".format("ID CODE", "LAST NAME", "FIRST NAME", "AGE", "ALLEGIANCE"))

            print("\n{0:13}\t  {1:9}\t  {2:9}\t  {3:2}\t  {4:33}".format(id[guess], lName[guess], fName[guess], age[guess], alg[guess]))


        else: 
            print("\n{0} couldn't be found please try again!".format(search))

        twice = again()


        if twice == "y":

            men = 2

        else:
            print() 
            input("Press enter to go back to menu")

            men = menu()



    for i in range(0, len(lName) - 1):

        for x in range(0, len(lName) - 1):

            if lName[x] > lName[x + 1]:

                switch(fName, x)
                switch(lName, x)
                switch(age, x)
                switch(id, x)

    if men == 3: #Seq search method 
        print() 
        search = input("Please enter in the last name you are looking for: ")

        flag = -1
        headcount = 0 

        for i in range(0, len(lName)):

            if search == lName[i]:

                headcount += 1

                if headcount == 1:

                    print("\n{0:13}\t  {1:9}\t  {2:9}\t  {3:2}\t  {4:33}".format("ID CODE", "LAST NAME", "FIRST NAME", "AGE", "ALLEGIANCE"))
                    print() 

                flag = i

                print("{0:13}\t  {1:9}\t  {2:9}\t  {3:2}\t  {4:33}".format(id[i], lName[i], fName[i], age[i], alg[i]))

        if flag == -1:

            print("\nCouldn't find {0}!".format(search))

        twice = again()

        
        if twice == "y":

            men = 3

        else:
            
            input("\nPress enter to go back to menu")
            men = menu()


    if men == 4:

        search = input("\nPlease enter in the allegiance you are looking for: ")

        flag = -1

        counter = 0 

        for i in range(0, len(alg)):

            if search == alg[i]:

                counter += 1

                if counter == 1:

                    print("\n{0:13}\t  {1:9}\t  {2:9}\t  {3:2}\t  {4:33}".format("ID CODE", "LAST NAME", "FIRST NAME", "AGE", "ALLEGIANCE"))


                flag = i

                print("{0:13}\t  {1:9}\t  {2:9}\t  {3:2}\t  {4:33}".format(id[i], lName[i], fName[i], age[i], alg[i]))

        if flag == -1:

            print("Couldn't find {0}!".format(search))


        twice = again()


        if twice == "y":

            men = 4

        else:
            input("Press enter to go back to menu")

            men = menu()


    if men == 5:

        print() 
        print("If you think this has a happy ending you haven’t been paying attention.")
        print() 
        input("Press enter.")
        
        answer = "B"

        clear()