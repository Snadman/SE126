#Name: Ethan Carrera
#Date: 8/8/2021
#Lab: 3A

#Variable Dictionary:
#

#Determine how much it would cost the company to replace all the machines from !2016! and EARLIER.

#Desktops $2,000
#Laptops $1,500

#--------------------------------------------------------------------------------------

   #Empty lists

type = []

brand = []

cpu = []

ram = []

oneDisk = []

hdd = []

twodisk = []

os = []

yr = []

record = 0

#how many desktops
desktop = 0

#desktop Costs
dCost = 2000

#desktop max value

dValue = 0



#how many laptops
laptops = 0

#laptop costs
lCost = 1500

#laptop value

lValue = 0


#If there is a 2 in HDD we need to change the numbers in which the OS and the YR take place

#To do this I remember to have multiple if statments 

import csv

#allows the opening of the labs 
with open("/Classes/SE126/Lab3/CSV/lab3a.csv") as csvfile:

    #Lab3\CSV\lab3a.csv
    file = csv.reader(csvfile)

    #Empty lists
    for rec in file:
        record += 1

        type.append(rec[0])

        brand.append(rec[1])

        cpu.append(rec[2])

        ram.append(rec[3])

        oneDisk.append(rec[4])

        hdd.append(int(rec[5]))
            #depending on this the twoDisk , OS and the YR is different

        #twodisk.append(rec[6])

        #OS

        #YR

        if int(rec[5]) == 1:
            
            twodisk.append(" ")
            os.append(rec[6])
            yr.append(int(rec[7]))
        
        elif int(rec[5]) == 2:

            twodisk.append(rec[6])
            os.append(rec[7])
            yr.append(int(rec[8]))

#no longer connected to the file  

        #this will make it so that everything corresponds to everything i.e for the records who have 1 or 2 HDDs and then it will now be going into the math to figure out how much money the boss will be sending


        #math

for i in range(0, record):

    if yr[i] <= 16:
        if type[i] == "D":
            
            desktop += 1
            
            #dValue += dCost

        elif type[i] == "L":
            
            laptops += 1

            #lValue += lCost

        
dValue = desktop * dCost

lValue = laptops * lCost


        
    
print("\n\nTo replace {0} it will cost ${1}".format(desktop,dValue))
print("\n\nTo replace {0} it will cost ${1}".format(laptops,lValue))
