#Name: Ethan Carrera
#Date: 8/1/2021
#Lab B

#Dictionary
#total_computer = amount of computers there are 
#total_desktop = amount of desktops there are
#total_laptops = amount of laptops there are
#

#--------------------------------------------------------------

import csv

total_computers = 0

total_desktop = 0

total_laptops = 0

total_2ndDrive = 0

print("{0:10} \t {1:10} \t {2:6} \t {3:10} \t {4:10} \t {5:10} \t {6:15} \t{7} \t{8}    |" .format("TYPE", "BRAND", "CPU","RAM","1ST DISK","NO HDD","2ND DISK","OS",'YR'))
print("---------------------------------------------------------------------------------------------------------------------------------------")


with open("/Classes/SE126/Lab2/Lab2_CSV/lab2b.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        total_computers += 1

        #type of computer (desktop v laptop)
        type = rec[0]

        #Company brand
        brand = rec[1]

        #CPU type
        cpu = rec[2]

        #Ram amount
        ram = rec[3]

        #1st disk storage
        oneDisk = rec[4]

        #Amount of HDD's
        hdd = int(rec[5])

        #2nd disk storage
        twoDisk = rec[6]

        #operating system
        #os = rec[7]

        #Yeah I have no idea what yr is 
        #yr = rec[8]

        #if the file says D it'll rewrite it to Desktop
        if(type == "D"):
            total_desktop += 1
            type = 'Desktop'

        #if the file says L it'll rewrite it to Laptop

        #rewriting L as to Laptops
        elif(type == "L"):
            total_laptops += 1
            type = 'Laptop'
        

        #BRAND RENAMING
        if(brand == "DL"):
            brand = 'Dell'
        
        elif(brand == "HP"):
            brand = 'HP'
        
        elif(brand == "GW"):
            brand = 'GateWay'

        if(hdd ==1):
            if(ram=='8'):
                ram = '08'
            
            else:
            #ram stays the same not putting a zero infront of 16
                ram = ram

            #since there are no HD2's the array # for the os and the yr changes and are reduced by one
            os = rec[6]
            yr = rec[7]
            print("{0}\t\t{1:18}{2:15}{3:18}{4:16}{5}\t\t\t\t\t{6}\t{7}".format(type,brand,cpu,ram,oneDisk,hdd,os,yr))

        elif(hdd == 2):

            if(ram=='8'):
                ram = '08'
            
            else:
                #ram stays the same not putting a zero infront of 16
                ram = ram
            
            total_2ndDrive += 1

            os = rec[7]
            yr = rec[8]
            print("{0}\t\t{1:18}{2:15}{3:18}{4:16}{5}\t\t  {6}\t\t\t{7}\t{8}".format(type,brand,cpu,ram,oneDisk,hdd,twoDisk,os,yr))

    
    print("__________________________________________________________________________________________________________________________________________")
    print("Number of computers:\t {0} \n" .format(total_computers))
    print("Out of the {0} computers only {1} are desktops\n".format(total_computers,total_laptops))
    print("Out of the {0} computers only {1} are laptops\n".format(total_computers,total_laptops))
    print("Only {0} of them have a 2nd Disk Drive".format(total_2ndDrive))