#Name: Ethan Carrera
#Date: 9/6/2021
#Lab B
#---------------------------------------
#Variable Dictionary
#
#
#
#
#
#
#---------------------------------------


import csv

#Clearing and sleeping-----------------


from os import system, name 
from time import sleep 
  
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 






#Functions-------------------------------------------
def pRow():

    row = int(input("\nSelect the row you want to sit in! \n[1-7]: "))

    while row < 1 or row > 7:

        print("That in not a valid response please try again.")
        row = int(input("\nPlease select the row you want to sit in! "))
    
    return row

def cSeat():

    seat = input("\nPlease select the seat where you would like to be seated \n[A-D]: ")

    seat = seat.upper()

    while seat != "A" and seat != 'B' and seat != 'C' and seat != 'D':
        print("\nThat in not a valid response please try again.")
        seat = input("\nPlease select the seat where you would like to be seated [A-D]: ")

    return seat


#def tryAgain():

   # answer = input("\nDo you want to pick another seat?[y/n]: ")

   # answer = answer.lower()

   # while answer != "y" and answer != "n":
   #     print("\nThat is not a valid response please try again.")
  #      answer = input("Do you want to pick another seat?")
    
  #  return answer




#A = ["A", "A", "A", "A", "A", "A", "A"]#0
#B = ["B", "B", "B", "B", "B", "B", "B"]#1
#C = ["C", "C", "C", "C", "C", "C", "C"]#2
#D = ["D", "D", "D", "D", "D", "D", "D"]#3


A = []
B = []
C = []
D = []


with open("Lab6/CSV/lab6B.CSV") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        
        A.append(rec[0])
        B.append(rec[1])
        C.append(rec[2])
        D.append(rec[3])
        

for i in range(0,7):
    print("{0})\t{1:5}{2:5}{3:5}{4:5}".format(i + 1, A[i], B[i], C[i], D[i]))


answer = "y"

while answer == "y":
    rows = pRow()
    seats = cSeat()

    print("You have chosen to sit at: {0}{1}" .format(rows,seats))

    correct = input("Is this correct?: [y/n]")

    while correct != "n" and correct != "y":
        print("ERROR PLEASE TRY AGAIN")

        print("You have chosen to sit at: {0}{1}" .format(rows,seats))
        correct = input("Is this correct?: [y/n]")

    if correct == "n":
        answer = "y"
    
    elif correct == "y":
        print("That's great! lets continue!")

        
        
        if seats == "A":
            if A[rows - 1] == "X":
                print("This seat is not available sorry!")

                for i in range(0, 7):
                    print("{0}\t {1} \t{2} \t   {3} \t{4} ".format(i + 1, A[i], B[i], C[i], D[i]))
            
            elif A[rows - 1] != "X":
                A[rows -1] = "X"

                for i in range(0, 7):
                    print("{0}\t {1} \t{2} \t   {3} \t{4} ".format(i + 1, A[i], B[i], C[i], D[i]))


        
        
        if seats == "B":
            
            if B[rows - 1] == "X":
                print("This seat is not available sorry!")

                for i in range(0, 7):
                    print("{0}\t {1} \t{2} \t   {3} \t{4} ".format(i + 1, A[i], B[i], C[i], D[i]))
            
            elif B[rows - 1] != "X":
                B[rows -1] = "X"

                for i in range(0, 7):
                    print("{0}\t {1} \t{2} \t   {3} \t{4} ".format(i + 1, A[i], B[i], C[i], D[i]))
        
        
        
        
        if seats == "C":
            
            if C[rows - 1] == "X":
                print("This seat is not available sorry!")

                for i in range(0, 7):
                    print("{0}\t {1} \t{2} \t   {3} \t{4} ".format(i + 1, A[i], B[i], C[i], D[i]))
            
            elif C[rows - 1] != "X":
                C[rows -1] = "X"

                for i in range(0, 7):
                    print("{0}\t {1} \t{2} \t   {3} \t{4} ".format(i + 1, A[i], B[i], C[i], D[i]))
        
        
        
        
        if seats == "D":
            
            if D[rows - 1] == "X":
                print("This seat is not available sorry!")

                for i in range(0, 7):
                    print("{0}\t {1} \t{2} \t   {3} \t{4} ".format(i + 1, A[i], B[i], C[i], D[i]))
            
            elif D[rows - 1] != "X":
                D[rows -1] = "X"

                for i in range(0, 7):
                    print("{0}\t {1} \t{2} \t   {3} \t{4} ".format(i + 1, A[i], B[i], C[i], D[i]))
        
    answer = input("\nDo you want to pick another seat?[y/n]: ")

    answer = answer.lower()

    while answer != "y" and answer != "n":
        print("\nThat is not a valid response please try again.")
        answer = input("Do you want to pick another seat?")

print("\n\n\nThank you for using me!\n\n")
print("Final look!\n")
for i in range(0, 7):
    print("{0}\t {1} \t{2} \t   {3} \t{4} ".format(i + 1, A[i], B[i], C[i], D[i]))