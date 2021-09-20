#Ethan Carrera
#Date: 8/30/2021
#lab: A


#Variable Dictionary:



#--------------------------------------------------------------------------------

import csv

total = 0
lname = []  #last name
fname = []  #First Name
bDay = []   #Birthday


print("{0}\t{1}\t{2}".format("Index  Last name", "First name", "Date of birth"))

#clocating file
with open ("/Classes/SE126/Lab5/txt/lab5.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file: 

        total += 1 
        l1 = rec[0] 
        f1 = rec[1] 
        d1 = rec[2]


        #appending each file
        lname.append(l1)
        fname.append(f1)
        bDay.append(d1)

    for i in range(0,total): #displaying the data 

     print("{0:2}\t{1:11}\t{2:3}\t\t{3}".format(i, lname[i], fname[i], bDay[i]))




#SEQUENTIAL SEARCH!
answer = "y"

while answer == "y": 
    search = input("Enter the birthday of who you are looking for? ")

    #flag system 
    flag = "red"
    location = -1 

    counter = 0 



    for i in range(0,total): 
        counter += 1 
        
        if search == bDay[i]:
            print("\nWe found the birthday person of who you're looking for!")

            location = i 
            print("\n\nThe search completed after {0} loops".format(counter))

            x = location

            flag = "green"

            #AGE BONUS

            a = search.split("/")

            year = int(a[2])

            age = 2021 - year


            print("Your search for {0} was found!".format(search))
            print("{0}) Name: {1} {2} \t|\tBirthday: {3}\t|\tAGE ≈  {4}" .format(x,fname[x],lname[x],bDay[x],age))

            
    if flag == "green":
                
        answer = input("\nDo you want to look for someone else?\n[y/n]: ")
        answer = answer.lower()

    if flag =="red":
        
        print("\nERROR NOT A VALID NAME\n")
        answer = input("\nDo you want to look for someone else?\n[y/n]: ")
        answer = answer.lower()

       
print("\n\nTHANK YOU FOR USING THIS PROGRAM HAVE A NICE DAY")


