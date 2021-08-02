#Name: Ethan Carrera
#Date: 7/31/2021
#lab A

#Dictionary:

# total_RecordCount = counting how many records there are in total
# total_limitCount = how many of the records go pass the limit 



#-------------------------------------------------------------------------------------

import csv #importing csv 

#Record counting 
total_RecordCount = 0

#Limit counting
total_LimitCount = 0

#room = the room name

#max = the max the room can hold

#min = the min people coming 

#over = how much they're over by


#NAMES OF THE COLLUM THINGS
print("{0:10} \t\t{1:5}\t{2:5}\t{3:5}".format("ROOM NAMES","MAX","MIN","OVER"))

#allows the opening of the labs 
with open("/Classes/SE126/Lab2/Lab2_CSV/lab2a.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:

        total_RecordCount += 1

        #room name
        room = rec[0]

        #room max limit
        max = int(rec[1])

        #room min limit
        min = int(rec[2])

        #how much it's over by
        over = abs(int(max - min))

        #if the minimum people who come is larger than the room 
        if(min > max):
            #counting how many files are valid
            total_LimitCount += 1

            print("{0:23} {1} \t{2} \t{3}".format(room,max,min,over))
        

    
    print("__________________________________________________")
    print("Processed {0} records \n" .format(total_RecordCount))
    print("There are {0} rooms over the limit.".format(total_LimitCount))




