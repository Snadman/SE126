#Name: Ethan Carrera
#Date: 8/17/2021
#Lab 3B

#this lab is about the voting process and who can and cannot be a voter aka invalid or not

#-------------NOTES--------------
#ID number
#age
#if the person is registered to vote
# if the person voted.

#--------VARIABLE DICTIONARY--------------



#idNum = the ID number

#age = the age of the users in the 

#1
#num_indv_netr = number of individuals not eligable to register

#2
#num_ageE_hvnR = number of individuals who are old enough to vote but have not registered

#3
#num_elgV_hvnV = who are eligable to vote but have not

#4
#num_indv_dvote = who did vote

#5
#Records: TO count how many times the loop goes and how many records are there

#LISTS



#-------------BASE-PROGRAM-CODE------------------

import csv
from os import terminal_size


#1
num_indv_netr = 0
one = num_indv_netr

#2
num_ageE_hvnR = 0
two = num_ageE_hvnR

#3
num_elgV_hvnV = 0
three = num_elgV_hvnV

#4
num_indv_dvote = 0
four = num_indv_dvote

#5
records = 0

#LISTS

uno = []
dos = []
tres = []
cuatro = []

print("\n\t\t----Welcome!----")

with open("D:/Classes/SE126/Lab3/CSV/lab3b.csv") as csvfile:
    
    file = csv.reader(csvfile)

    for rec in file:
        records += 1

        field0 = rec[0] #id
        field1 = int(rec[1]) #age
        field2 = rec[2] #rv
        field3 = rec[3] #voted

        #1
        if field1 < 18:
            one += 1

        #2
        elif field1>=18 and field2 == 'N':
            two += 1
        
        elif field1>18 and field2 == 'Y' and field3=='N':
            three += 1
        
        elif field1>18 and field2 == 'Y' and field3=='Y':
            four += 1

        #----list Storage----
        uno.append(field0)
        dos.append(field1)
        tres.append(field2)
        cuatro.append(field3)

#outside the file loop

#1
print("\n\n1. Number of individuals not eligible to register: {0}".format(one))

#2
print("\n\n2: Number of individuals who are old enough to vote but have not registered: {0}".format(two))

#3
print("\n\n3. Number of individuals who are eligible to vote but did not vote: {0}".format(three))

#4
print("\n\n4. Number of individuals who did vote: {0}".format(four))

#5
print("\n\n5. Number of records processed: {0}" .format(records))




            

