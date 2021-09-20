#NAME: Ethan Carrera
#Date: 8/24/2021
#Lab: 4A

#Variable Dictionary


#The lists are self indetifiable 

#houseA = house name

#motto = house motto

#c_stark = are counting how many "users" are in the house that comes after the _
#c_watch = are counting how many "users" are in the house that comes after the _
#c_tully = are counting how many "users" are in the house that comes after the _
#c_lannister = are counting how many "users" are in the house that comes after the _
#c_baratheon = are counting how many "users" are in the house that comes after the _
#c_targaryen = are counting how many "users" are in the house that comes after the _



#------------------------

#COLOR CLASS
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


#--------------





import csv



total = 0
firstName = []
lastName = []
age = []
nickName = []
houseA = []

#for part 2 of lab A

#motto = []

print(color.BOLD+color.UNDERLINE+"Index \tFirst Name \tLast Name \tAge \tNick Name \t\tHouse"+color.END)

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
    
    
for i in range(0,total):
    print("{0:2}\t{1:15}\t{2:10}\t{3:2}\t{4:20}\t{5:2}\n".format(i,firstName[i],lastName[i],age[i],nickName[i],houseA[i]))

print(color.BOLD+"------------------------------------------------------------------------------------------------------------------------"+color.END)

print(color.BOLD+color.UNDERLINE+"Index\tFirst Name\tLast Name\tAge\tNick Name\t\tHouse\t\t\tMotto"+color.END)

print(color.BOLD+"------------------------------------------------------------------------------------------------------------------------"+color.END)

#counting
c_stark = 0
c_watch = 0
c_tully = 0
c_lannister = 0
c_baratheon = 0
c_targaryen = 0

for i in range(0,total):
    if houseA[i] == "House Stark":

        motto = "Winter Is Coming"

        c_stark += 1


    if houseA[i] == "House Baratheon":

        motto = "Ours is the fury"

        c_baratheon += 1


    if houseA[i] == "House Tully":

        motto = "Family.Duty.Honor"

        c_tully += 1


    if houseA[i] == "Night's Watch":

        motto = "And now my watch begins."

        c_watch += 1



    if houseA[i] == "House Lannister":

        motto = "Hear me roar!."

        c_lannister += 1


    elif houseA[i] == "House Targaryen":

        motto = "Fire & Blood."

        c_targaryen += 1


    print("\n{0:2}\t{1:15}\t{2:10}\t{3:2}\t{4:20}\t{5:2}\t\t{6:10}\n".format(i,firstName[i],lastName[i],age[i],nickName[i],houseA[i],motto))
    print("________________________________________________________________________________________________________________________")

print(color.BOLD+"\n\n------------------------------------------------------------------------------------------------------------------------"+color.END)

totalA = 0 #total age

for i in range(0,total):
    totalA += age[i]

avg_A = totalA / total



print(color.GREEN+"TOTAL AMOUNT OF PEOPLE:{0} ".format(total)+color.END)

print(color.RED+"Average Age (rounded): {0:.0f}\n".format(avg_A)+color.END)

print(color.YELLOW+"COUNT PER ALLEGIANCE\n")

print(color.YELLOW+'STARK\t\tWATCH\t\tTULLY\t\tLANNISTER\t\tBARATHEON\t\tTARGARYEN\t\t'+color.END)
print("{0}\t\t{1}\t\t{2}\t\t{3}\t\t\t{4}\t\t\t{5}".format(c_stark,c_watch,c_tully,c_lannister,c_baratheon,c_targaryen))



#       print(color.YELLOW+'STARK'+color.END)
#       print(color.YELLOW+"Num AMT: {0}".format(c_stark))
#       for i in range(0,c_stark):
#           print("I")
#       
#       print(color.YELLOW+'WATCH'+color.END)
#       print(color.YELLOW+"Num AMT: {0}".format(c_watch))
#       for i in range(0,c_stark):
#           print("I")
#       
#       print(color.YELLOW+'TULLY'+color.END)
#       print(color.YELLOW+"Num AMT: {0}".format(c_tully))
#       for i in range(0,c_stark):
#           print("I")
#       
#       print(color.YELLOW+'LANNISTER'+color.END)
#       print(color.YELLOW+"Num AMT: {0}".format(c_lannister))
#       for i in range(0,c_stark):
#           print("I")
#       
#       print(color.YELLOW+'BARATHEON'+color.END)
#       print(color.YELLOW+"Num AMT: {0}".format(c_baratheon))
#       for i in range(0,c_stark):
#           print("I")
#       
#       print(color.YELLOW+'TARGARYEN'+color.END)
#       print(color.YELLOW+"Num AMT: {0}".format(c_targaryen))
#       for i in range(0,c_stark):
#           print("I")