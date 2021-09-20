#Name : Ethan Carrera
#Date: 8/24/2021

#variable dictionary

#The lists are self indetifiable 

#houseA = house name

#houseM = house motto

# def one() = will print out first name, last name and nicknames

# def two() = will print out last name, house and motto

# def three() = will print out all of them including the motto 

# def menu() = will print out the menu and this is where everthing comes together asking if the user wants to go to def 1-3 and if they choose 4 it'll take them out and print out a goodbye statement and that will stop the program


#userInput = is just the userinput what they decide to use and such

#loop = is the while loop indiciative allowing for it to run or to cease

#----------------------------------------------------

#import 

import csv


#----------------------------------------------------

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


#----------------------------------------------------

#Empty lists

firstName = []
lastName = []
age = []
nickName = []
houseA = []
houseM = []

#TOTAL TOO




#-------------------------------------------------
#functions

#1

def one():
    #first , last and nicknames

    print(color.BOLD+"------------------------------------------------------------------------------------------------------------------------"+color.END)

    print(color.BOLD+color.UNDERLINE+"Index\tFirst Name\t\tLast Name\t\t\tNick Name"+color.END)

    print(color.BOLD+"------------------------------------------------------------------------------------------------------------------------"+color.END)

    for i in range(0,total):

        print("\n{0:2}\t{1:15}\t\t{2:10}\t\t\t{3:2}\n".format(i,firstName[i],lastName[i],nickName[i]))
        print("________________________________________________________________________________________________________________________")
        





#-----------------------------------------------------
#2

def two():
    #last house and motto

    print(color.BOLD+"------------------------------------------------------------------------------------------------------------------------"+color.END)

    print(color.BOLD+color.UNDERLINE+"Index\tLast Name\t\tHouse\t\t\t\t\t\tMotto"+color.END)

    print(color.BOLD+"------------------------------------------------------------------------------------------------------------------------"+color.END)

    for i in range(0,total):

        print("\n{0:2}\t{1:15}\t\t{2:45}{3}\n".format(i,lastName[i],houseA[i],houseM[i]))
        print("________________________________________________________________________________________________________________________")
    

#---------------------------------------------------
#3

def three():

    print(color.BOLD+"------------------------------------------------------------------------------------------------------------------------"+color.END)

    print(color.BOLD+color.UNDERLINE+"Index\tFirst Name\tLast Name\tAge\tNick Name\t\tHouse\t\t\tMotto"+color.END)

    print(color.BOLD+"------------------------------------------------------------------------------------------------------------------------"+color.END)

    for i in range(0,total):

        print("\n{0:2}\t{1:15}\t{2:10}\t{3:2}\t{4:20}\t{5:2}\t\t{6:10}\n".format(i,firstName[i],lastName[i],age[i],nickName[i],houseA[i],houseM[i]))
        print("________________________________________________________________________________________________________________________")

#_________________________________________________________________________________________________________________________________________________________________________________________________


def menu():
    
    print("Hello! please choose an option.")
    print("\n1. Print all First,Last, and nicknames\n\n2. Print Last names with House Allegiance and Motto\n\n3. Print full records\n\n4.  Exit")

    userinput = input("Input[1-4]: ")

    loop = 'y'

    while loop == 'y':

        if userinput == '1':
            one()

            loop = input("Do you want to continue? [y/n]: ")
            
            if loop == 'y':
                userinput = input("Which one would you like now?[1-4]: ")
            
            else:
                print()


        
        elif userinput =='2':
            two()

            loop = input("Do you want to continue? [y/n]: ") 

            if loop == 'y':
                userinput = input("Which one would you like now?[1-4]: ")
            
            else:
                print()


        elif userinput == '3':
            three()

            loop = input("Do you want to continue? [y/n]: ")

            if loop == 'y':
                userinput = input("Which one would you like now?[1-4]: ")
            
            else:
                print()

        
        elif userinput == '4':
            loop = 'n'

        else:
            print("Error 606")
            loop = input("Do you want to continue? [y/n]: ")
    
    print("Thank You! Goodbye!")
        

#---------------------------------------------------


#main code 

total = 0
#CSV FILE
with open("/Classes/SE126/Lab4/CSV_files/lab4.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        total += 1
        fn = rec[0]
        ln = rec[1]
        a = int(rec[2])
        nn = rec[3]
        ha = rec[4]
        
        firstName.append(fn)
        lastName.append(ln)
        age.append(a)
        nickName.append(nn)
        houseA.append(ha)

#APPENDING MOTTO

    for i in range(0,total):
        if houseA[i] == "House Stark":
            
            houseM.append("Winter Is Coming")

        if houseA[i] == "House Baratheon":

            houseM.append("Ours is the fury")

        if houseA[i] == "House Tully":

            houseM.append("Family.Duty.Honor")

        if houseA[i] == "Night's Watch":

            houseM.append("And now my watch begins.")

        if houseA[i] == "House Lannister":

            houseM.append("Hear me roar!")

        elif houseA[i] == "House Targaryen":

            houseM.append("Fire & Blood.")


menu()