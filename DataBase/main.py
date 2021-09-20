#Name: Ethan Carrera
#Date: 9/8/2021

#the point of this file is to show the gap between both main and female with seperation of race and then the addition at the end of all the races. Three different graphs to show the three differnet levels of numbers. It also goes without saying that we're looking at the 

#------------------------------------------------------------------------------


#This is the colors to make it look nice i guess


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   GRAY = '\033[95m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'




#-----------------------------------------------------------------------------

#importing csv
import csv

from pandas.core.frame import DataFrame 



#we'll have to set the total of all the different male income to one total so we can see the average differance 




#Every Total total average income  for males 
TMAI = []


#Total total average income  for females 
TFAI = []


#Amount of records we've gone through 

tTotal = []

#-------------------------MALES--------------------------------
#American Indian Male 
def AI():

    #globalizing tTotal 

    global tTotal 

    global AIMincome

    #total income in this file 
    AIMtotal = 0

    



    id = []
    location = []
    AIMincome = []

    with open("DataBase/DataMan/Male/Indian_Male.csv") as AIM:

        afile = csv.reader(AIM)

        #records total 

        records = 0

        for rec in afile:
            n = rec[0]
            l = rec[1]
            i = int(rec[2])

            records += 1

            id.append(n)
            location.append(l)
            AIMincome.append(i)

    #valid individuals with income so we can divide it by the correct ammount to get the average total 
    vPeople = 0
   

    for i in range(0,records):
        
        if AIMincome[i] > 0:
            vPeople += 1

        elif AIMincome[i] == 0:
            vPeople += 0
    
    
    #average of the total 
    total = sum(AIMincome)

    AIMtotal = total / vPeople

    
    

    #estimated to the nearest whole number
    print(color.GREEN+"\n\nThe average Household Income at Age 35 for American indian males is : ${0:0.0f}".format(AIMtotal)+color.END)

    tTotal.append(1)

    TMAI.append(AIMtotal)


#American American Asian Male 
def AA():

    #globalizing tTotal 

    global tTotal 

    global AIMincome

    #total income in this file 
    AIMtotal = 0

    



    id = []
    location = []
    AIMincome = []

    with open("DataBase/DataMan/Male/Asian_Male.csv") as AIM:

        afile = csv.reader(AIM)

        #records total 

        records = 0

        for rec in afile:
            n = rec[0]
            l = rec[1]
            i = int(rec[2])

            records += 1

            id.append(n)
            location.append(l)
            AIMincome.append(i)

    #valid individuals with income so we can divide it by the correct ammount to get the average total 
    vPeople = 0
   

    for i in range(0,records):
        
        if AIMincome[i] > 0:
            vPeople += 1

        elif AIMincome[i] == 0:
            vPeople += 0
    
    
    #average of the total 
    total = sum(AIMincome)

    AIMtotal = total / vPeople

    
    

    #estimated to the nearest whole number
    print(color.RED+"\n\nThe average Household Income at Age 35 for Asian American males is : ${0:0.0f}".format(AIMtotal)+color.END)

    tTotal.append(1)

    TMAI.append(AIMtotal)


#Black American Male
def BA():

    #globalizing tTotal 

    global tTotal 

    global AIMincome

    #total income in this file 
    AIMtotal = 0

    



    id = []
    location = []
    AIMincome = []

    with open("DataBase/DataMan/Male/Black_Male.csv") as AIM:

        afile = csv.reader(AIM)

        #records total 

        records = 0

        for rec in afile:
            n = rec[0]
            l = rec[1]
            i = int(rec[2])

            records += 1

            id.append(n)
            location.append(l)
            AIMincome.append(i)

    #valid individuals with income so we can divide it by the correct ammount to get the average total 
    vPeople = 0
   

    for i in range(0,records):
        
        if AIMincome[i] > 0:
            vPeople += 1

        elif AIMincome[i] == 0:
            vPeople += 0
    
    
    #average of the total 
    total = sum(AIMincome)

    AIMtotal = total / vPeople

    
    

    #estimated to the nearest whole number
    print(color.PURPLE+"\n\nThe average Household Income at Age 35 for Black American males is : ${0:0.0f}".format(AIMtotal)+color.END)

    tTotal.append(1)

    TMAI.append(AIMtotal)

#Hispanic American Male
def HA():

    #globalizing tTotal 

    global tTotal 

    global AIMincome

    #total income in this file 
    AIMtotal = 0

    



    id = []
    location = []
    AIMincome = []

    with open("DataBase/DataMan/Male/Hispanic_Male.csv") as AIM:

        afile = csv.reader(AIM)

        #records total 

        records = 0

        for rec in afile:
            n = rec[0]
            l = rec[1]
            i = int(rec[2])

            records += 1

            id.append(n)
            location.append(l)
            AIMincome.append(i)

    #valid individuals with income so we can divide it by the correct ammount to get the average total 
    vPeople = 0
   

    for i in range(0,records):
        
        if AIMincome[i] > 0:
            vPeople += 1

        elif AIMincome[i] == 0:
            vPeople += 0
    
    
    #average of the total 
    total = sum(AIMincome)

    AIMtotal = total / vPeople

    
    

    #estimated to the nearest whole number
    print(color.YELLOW+"\n\nThe average Household Income at Age 35 for Hispanic American males is : ${0:0.0f}".format(AIMtotal)+color.END)

    tTotal.append(1)

    TMAI.append(AIMtotal)

#White American Male 

def WA():

    #globalizing tTotal 

    global tTotal 

    global AIMincome

    #total income in this file 
    AIMtotal = 0

    



    id = []
    location = []
    AIMincome = []

    with open("DataBase/DataMan/Male/White_Male.csv") as AIM:

        afile = csv.reader(AIM)

        #records total 

        records = 0

        for rec in afile:
            n = rec[0]
            l = rec[1]
            i = int(rec[2])

            records += 1

            id.append(n)
            location.append(l)
            AIMincome.append(i)

    #valid individuals with income so we can divide it by the correct ammount to get the average total 
    vPeople = 0
   

    for i in range(0,records):
        
        if AIMincome[i] > 0:
            vPeople += 1

        elif AIMincome[i] == 0:
            vPeople += 0
    
    
    #average of the total 
    total = sum(AIMincome)

    AIMtotal = total / vPeople

    
    

    #estimated to the nearest whole number
    print(color.CYAN+"\n\nThe average Household Income at Age 35 for White American males is : ${0:0.0f}".format(AIMtotal)+color.END)

    tTotal.append(1)

    TMAI.append(AIMtotal)

#---------------------------------------------------------------

#----------------------FEMALES----------------------------------

#American Indian Female 
def AIF():

    #globalizing tTotal 

    global tTotal 

    global AIMincome

    #total income in this file 
    AIMtotal = 0

    



    id = []
    location = []
    AIMincome = []

    with open("DataBase/DataMan/Female/AmerIndian_Female.csv") as AIM:

        afile = csv.reader(AIM)

        #records total 

        records = 0

        for rec in afile:
            n = rec[0]
            l = rec[1]
            i = int(rec[2])

            records += 1

            id.append(n)
            location.append(l)
            AIMincome.append(i)

    #valid individuals with income so we can divide it by the correct ammount to get the average total 
    vPeople = 0
   

    for i in range(0,records):
        
        if AIMincome[i] > 0:
            vPeople += 1

        elif AIMincome[i] == 0:
            vPeople += 0
    
    
    #average of the total 
    total = sum(AIMincome)

    AIMtotal = total / vPeople

    
    

    #estimated to the nearest whole number
    print(color.GREEN+"\n\nThe average Household Income at Age 35 for American Indian females is : ${0:0.0f}".format(AIMtotal)+color.END)

    tTotal.append(1)

    TFAI.append(AIMtotal)

#American Asian Female
def AAF():

    #globalizing tTotal 

    global tTotal 

    global AIMincome

    #total income in this file 
    AIMtotal = 0

    



    id = []
    location = []
    AIMincome = []

    with open("DataBase/DataMan/Female/Asian_Female.csv") as AIM:

        afile = csv.reader(AIM)

        #records total 

        records = 0

        for rec in afile:
            n = rec[0]
            l = rec[1]
            i = int(rec[2])

            records += 1

            id.append(n)
            location.append(l)
            AIMincome.append(i)

    #valid individuals with income so we can divide it by the correct ammount to get the average total 
    vPeople = 0
   

    for i in range(0,records):
        
        if AIMincome[i] > 0:
            vPeople += 1

        elif AIMincome[i] == 0:
            vPeople += 0
    
    
    #average of the total 
    total = sum(AIMincome)

    AIMtotal = total / vPeople

    
    

    #estimated to the nearest whole number
    print(color.RED+"\n\nThe average Household Income at Age 35 for Asian American Females is : ${0:0.0f}".format(AIMtotal)+color.END)

    tTotal.append(1)

    TFAI.append(AIMtotal)

#Black American Female
def BAF():

    #globalizing tTotal 

    global tTotal 

    global AIMincome

    #total income in this file 
    AIMtotal = 0

    



    id = []
    location = []
    AIMincome = []

    with open("DataBase/DataMan/Female/Black_Female.csv") as AIM:

        afile = csv.reader(AIM)

        #records total 

        records = 0

        for rec in afile:
            n = rec[0]
            l = rec[1]
            i = int(rec[2])

            records += 1

            id.append(n)
            location.append(l)
            AIMincome.append(i)

    #valid individuals with income so we can divide it by the correct ammount to get the average total 
    vPeople = 0
   

    for i in range(0,records):
        
        if AIMincome[i] > 0:
            vPeople += 1

        elif AIMincome[i] == 0:
            vPeople += 0
    
    
    #average of the total 
    total = sum(AIMincome)

    AIMtotal = total / vPeople

    
    

    #estimated to the nearest whole number
    print(color.PURPLE+"\n\nThe average Household Income at Age 35 for Black American Females is : ${0:0.0f}".format(AIMtotal)+color.END)

    tTotal.append(1)

    TFAI.append(AIMtotal)

#Hispanic American Female 
def HAF():

    #globalizing tTotal 

    global tTotal 

    global AIMincome

    #total income in this file 
    AIMtotal = 0

    



    id = []
    location = []
    AIMincome = []

    with open("DataBase/DataMan/Female/Hispanic_Female.csv") as AIM:

        afile = csv.reader(AIM)

        #records total 

        records = 0

        for rec in afile:
            n = rec[0]
            l = rec[1]
            i = int(rec[2])

            records += 1

            id.append(n)
            location.append(l)
            AIMincome.append(i)

    #valid individuals with income so we can divide it by the correct ammount to get the average total 
    vPeople = 0
   

    for i in range(0,records):
        
        if AIMincome[i] > 0:
            vPeople += 1

        elif AIMincome[i] == 0:
            vPeople += 0
    
    
    #average of the total 
    total = sum(AIMincome)

    AIMtotal = total / vPeople

    
    

    #estimated to the nearest whole number
    print(color.YELLOW+"\n\nThe average Household Income at Age 35 for Hispanic American Females is : ${0:0.0f}".format(AIMtotal)+color.END)

    tTotal.append(1)

    TFAI.append(AIMtotal)

#White American Female
def WAF():

    #globalizing tTotal 

    global tTotal 

    global AIMincome

    #total income in this file 
    AIMtotal = 0

    



    id = []
    location = []
    AIMincome = []

    with open("DataBase/DataMan/Female/White_Female.csv") as AIM:

        afile = csv.reader(AIM)

        #records total 

        records = 0

        for rec in afile:
            n = rec[0]
            l = rec[1]
            i = int(rec[2])

            records += 1

            id.append(n)
            location.append(l)
            AIMincome.append(i)

    #valid individuals with income so we can divide it by the correct ammount to get the average total 
    vPeople = 0
   

    for i in range(0,records):
        
        if AIMincome[i] > 0:
            vPeople += 1

        elif AIMincome[i] == 0:
            vPeople += 0
    
    
    #average of the total 
    total = sum(AIMincome)

    AIMtotal = total / vPeople

    
    

    #estimated to the nearest whole number
    print(color.CYAN+"\n\nThe average Household Income at Age 35 for White American Females is : ${0:0.0f}".format(AIMtotal)+color.END)

    tTotal.append(1)

    TFAI.append(AIMtotal)
#---------------------------------------------------------------

#-------------------------MAIN-CODE-----------------------------

#Lists for avg income

EndAVGI = []

#-----------------


print(color.BOLD+color.UNDERLINE+color.DARKCYAN+"\n\nMALE CATEGORY"+color.END)
AI()

AA()

BA()

HA()

WA()

print()

#print(TMAI)

print(color.YELLOW+color.UNDERLINE+"Total income amount for males: ${0:0.0f}".format(sum(TMAI))+color.END)


#amount of races
AMTR = sum(tTotal)

#Sum of male income 
sumMI = sum(TMAI)

#Avergage male income
AVGMI = sumMI / AMTR

EndAVGI.append(AVGMI)

print(color.YELLOW+color.UNDERLINE+"\nAverage income amount for males: ${0:0.0f}".format(AVGMI)+color.END)



#------------------------  FEMALE   ----------------------

print(color.BOLD+color.UNDERLINE+color.GRAY+"\n\nFEMALE CATEGORY"+color.END)

AIF()

AAF()

BAF()

HAF()

WAF()

print()


print(color.YELLOW+color.UNDERLINE+"Total income amount for females: ${0:0.0f}".format(sum(TFAI))+color.END)

#sum of female income
sumFI = sum(TFAI)

#average female income
AVGFI = sumFI / AMTR

EndAVGI.append(AVGFI)

print(color.YELLOW+color.UNDERLINE+"\nAverage income amount for females: ${0:0.0f}".format(AVGFI)+color.END)
#print(TFAI)




#---------------------------------------------------------------

#-----------------------------PANDA TIME-------------------------

import pandas as pd
import matplotlib.pyplot as plt
import numpy as py




#TMAI for males 
#TFAI for females

races = ["American Indian", "Asian American","Black American","Hispanic American","White American"]

#Genders
Genders = ["Male","Female"]

mIncome = [15000,30000,45000,60000]

fIncome = [15000,30000,45000,61000]


#data frame male
DFM = pd.DataFrame(TMAI,columns=["AVG_Income"])

#Data frame Female
DFF = pd.DataFrame(TFAI,columns=['AVG_Income'])

#races
DFRace = pd.DataFrame(races,columns=["race"])

plt.bar(DFRace.race,DFM.AVG_Income,color=['seagreen','tomato','violet','orange','dodgerblue'])
plt.style.use('fivethirtyeight')
plt.ylabel('AVERAGE INCOME')
plt.xlabel('RACES')
plt.title('AVG MALE INCOME STATS')
plt.yticks(mIncome)
plt.show()

plt.bar(DFRace.race,DFF.AVG_Income,color=['seagreen','tomato','violet','orange','dodgerblue'])
plt.style.use('fivethirtyeight')
plt.ylabel('AVERAGE INCOME')
plt.xlabel('RACES')
plt.title('AVG FEMALE INCOME STATS')
plt.yticks(fIncome)
plt.show()

# AVGMI #male 
# #AVGFI #Female

DFGender = pd.DataFrame(Genders,columns=["Genders"]) 
DFFinal = pd.DataFrame(EndAVGI,columns=["Avg"])

plt.bar(DFGender.Genders,DFFinal.Avg,color=['orange','dodgerblue'])
plt.style.use('fivethirtyeight')
plt.ylabel('AVERAGE INCOME')
plt.xlabel('GENDERS')
plt.title('AVG GENDER INCOME STATS')
plt.yticks(fIncome)
plt.show()