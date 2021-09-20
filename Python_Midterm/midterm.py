#Jacob's and Ethan's midterm project
#8/20/2021
#--------------------------------------------------------------------------------------
#Note: We are using three csv files for our project 
#1 Food.csv
#2 Tech.csv 
#3 Clothing.csv
#Building a check list program and then you may check what you buy 
#Creating a while loop asking the user what they want to buy.
#---------------------------------------------------------------------------------------
#imports
import csv


#---------------------------------------------------------------------------------------

#Varible Dicitionary

#Total = will be the global total being used by every function so that the code can accuratly add it all up 

#TempTotal = will be the temporary total so that it shows the user how much money they'd be spending if they buy x amount of items before adding it to total so that if they don't want that many items they can just say no and try a different amount

#----------------------------------------------------------------
#name
#price
#stock
#ALL three of them are lists that are part of the CSV files and we're just appending the values to the list so we don't have to use rec[0] over and over and we get rid of the need to be coding inside the with open.

#iItem is the list of the amount of records i.e 1,2,3,4,5,6,7,etc

#----------------------------------------------------------------

#records are how many records there are in total from 1-X


#----------------------------------------------------------------
#n
#p
#s
#These are all the variables we're setting rec[i] to so i.e for the first time around it'll go 0 and then it'll append that to the 0 slot on the list and then it'll go to 1 and so on
#----------------------------------------------------------------

#choice will hold the users first choice for that specific question
#quantity will be how many items the user wants
#correction1 = same thing as correction just making sure that the user has inputed what they wanted

#----------------------------------------------------------------

#q1-4 are just questions 1-4 asking if the user which genre of shopping they want to go to 


#answer1 to make sure they want to exit


#---------------COLORS------------------------------
 #in this color code it's a class call color and when searching up changing color text these using an ANSI escape sequence I was able to make the class called color allowing me to use color.BLUE+ so that can use that instead of having to put "\033[94m" everytime I want to use the color blue

 #ansi means american national standard institute


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

#---------------------------------------------------


#----------------GLOBALS---------------------------------------------------------------
total = 0
#---------------------------------------------------------------------------------------

#Functions
def tech():


    #made total into a global for it to be used everywhere.
    global total
    
    #made total into a global for it to be used everywhere.
    
    print(color.RED+color.BOLD+color.UNDERLINE+"\n\nTechnology Items\n\n"+color.END)
    
    tempTotal = 0
    #EMPTY LISTS
    name = []
    price = []
    stock = []

    with open("/Classes/SE126/Python_Midterm/CSV/tech.csv") as techFile:
        tfile = csv.reader(techFile)

        #counters
        records = 0
        


        

        #iItem is the list of the amount of records i.e 1,2,3,4,5,6,7,etc
        iItem = []

        for rec in tfile:
            n = rec[0]
            p = float(rec[1])
            s = rec[2]

            records += 1

            name.append(n)
            price.append(p)
            stock.append(s)
            iItem.append(records)

    #-----------------------Options----------------------------------
    for i in range (0,records):                                 
        print(color.BOLD+color.YELLOW+color.UNDERLINE+"{0})".format(i+1)+color.RED+color.BOLD+" {0}:".format(name[i])+color.GREEN+color.BOLD+"${0}\n\n".format(price[i])+color.END)
    #----------------------------------------------------------------

    #entering loop
    loop ='y'


    while loop == 'y':

        choice = choice = int(input(color.UNDERLINE+color.YELLOW+"What would you like to order today?(Please choose from 1-{0}):\n\t".format(records)+color.END))  #records because the amount of records are the amount of rows we have in the csv file
            

        #This will allow the code to see if the choice the customer made was valid and then if it's within the threshold it'll print the item cost and ask how many of that specific item they'd want
        rekon = choice - 1
            

            #it has to be rekon because it's the users choice 1 would be 1 in the CSV file but not the 1 they want so we need to put choice - 1 so that it registers that when they want the first item it's 0 and the second item is 1 in the list

        if choice == iItem[rekon]:

            correction = input(color.YELLOW+"\nYou have selected {0} is that correct?[y/n]\n".format(name[rekon])+color.END)
            correction = correction.lower()

            if correction == 'y':
                print(color.RED+"\nGreat!\n"+color.END)

                quantity = int(input(color.BOLD+color.PURPLE+"\nHow many {0} are you planning on buying?\n\t***PLEASE BE ADVISED EACH {0} COSTS ${1}***\n".format(name[rekon],price[rekon])+color.END))

                #temporary total = quantity * the price of the specific item they want
                tempTotal = quantity * price[rekon]

                correction1 = input(color.YELLOW+"\n\n{0} {1}('s) will be ${2} is that ok?\n".format(quantity,name[rekon],tempTotal)+color.END)
                correction1 = correction1.lower()

                if correction1 == 'y':
                    total += tempTotal

                    #set tempTotal to 0 so that it'll reset and show you the price for only the bulk items you're planning on buying and not having it added with every loop

                    tempTotal = 0
                    loop = 'n'
                    
                elif correction1 == 'n':
                    tempTotal = 0
                    print(color.RED+"\n\nplease try again!\n\n"+color.END)
                        
                    
                elif correction1 != 'y' or correction1 !='n':
                    tempTotal = 0
                    loop = 'y'
                
            else:
                print(color.RED+"\n\nERROR\n\n"+color.END)
                loop = 'y'
            
        else: 
            print(color.RED+"\n\nERROR!\n\n"+color.END)
            loop = 'y'



        #exiting loop
        print(color.RED+"\nDo you want to continue shopping?"+color.END)
        loop = input(color.YELLOW+"\n[y/n] : "+color.END)
        loop.lower()

    return total
        
        
        
        
#----------------------clothing function----------------------------------------
def clothing():
    #made total into a global for it to be used everywhere.
    global total
    
    
    print(color.CYAN+color.BOLD+color.UNDERLINE+"\n\nClothing Items\n\n"+color.END)

    tempTotal = 0
    #EMPTY LISTS
    name = []
    price = []
    stock = []

    with open("/Classes/SE126/Python_Midterm/CSV/clothing.csv") as techFile:
        tfile = csv.reader(techFile)

        #counters
        records = 0
        


        

        #iItem is the list of the amount of records i.e 1,2,3,4,5,6,7,etc
        iItem = []

        for rec in tfile:
            n = rec[0]
            p = float(rec[1])
            s = rec[2]

            name.append(n)
            price.append(p)
            stock.append(s)
            records += 1
            iItem.append(records)

       #-----------------------Options----------------------------------
    for i in range (0,records):                                 
        print(color.BOLD+color.YELLOW+color.UNDERLINE+"{0})".format(i+1)+color.RED+color.BOLD+" {0}:".format(name[i])+color.GREEN+color.BOLD+"${0}\n\n".format(price[i])+color.END)
    #----------------------------------------------------------------

    #entering loop
    loop ='y'


    while loop == 'y':

        choice = choice = int(input(color.UNDERLINE+color.YELLOW+"What would you like to order today?(Please choose from 1-{0}):\n\t".format(records)+color.END))  #records because the amount of records are the amount of rows we have in the csv file
            

        #This will allow the code to see if the choice the customer made was valid and then if it's within the threshold it'll print the item cost and ask how many of that specific item they'd want
        rekon = choice - 1
            

            #it has to be rekon because it's the users choice 1 would be 1 in the CSV file but not the 1 they want so we need to put choice - 1 so that it registers that when they want the first item it's 0 and the second item is 1 in the list

        if choice == iItem[rekon]:

            correction = input(color.YELLOW+"\nYou have selected {0} is that correct?[y/n]\n".format(name[rekon])+color.END)
            correction = correction.lower()

            if correction == 'y':
                print(color.RED+"\nGreat!\n"+color.END)

                quantity = int(input(color.BOLD+color.PURPLE+"\nHow many {0} are you planning on buying?\n\t***PLEASE BE ADVISED EACH {0} COSTS ${1}***\n".format(name[rekon],price[rekon])+color.END))

                #temporary total = quantity * the price of the specific item they want
                tempTotal = quantity * price[rekon]

                correction1 = input(color.YELLOW+"\n\n{0} {1}('s) will be ${2} is that ok?\n".format(quantity,name[rekon],tempTotal)+color.END)
                correction1 = correction1.lower()

                if correction1 == 'y':
                    total += tempTotal

                    #set tempTotal to 0 so that it'll reset and show you the price for only the bulk items you're planning on buying and not having it added with every loop

                    tempTotal = 0
                    loop = 'n'
                    
                elif correction1 == 'n':
                    tempTotal = 0
                    print(color.RED+"\n\nplease try again!\n\n"+color.END)
                        
                    
                elif correction1 != 'y' or correction1 !='n':
                    tempTotal = 0
                    loop = 'y'
                
            else:
                print(color.RED+"\n\nERROR\n\n"+color.END)
                loop = 'y'
            
        else: 
            print(color.RED+"\n\nERROR!\n\n"+color.END)
            loop = 'y'



        #exiting loop
        print(color.RED+"\nDo you want to continue shopping?"+color.END)
        loop = input(color.YELLOW+"\n[y/n] : "+color.END)
        loop.lower()

    return total

#----------------------FOOD FUNCTION---------------------------------------------------------
def food():
    global total
    
    
    
    tempTotal = 0
    #EMPTY LISTS
    name = []
    price = []
    stock = []

    with open("/Classes/SE126/Python_Midterm/CSV/food.csv") as techFile:
        tfile = csv.reader(techFile)

        #counters
        records = 0
        


        

        #iItem is the list of the amount of records i.e 1,2,3,4,5,6,7,etc
        iItem = []

        for rec in tfile:
            n = rec[0]
            p = float(rec[1])
            s = rec[2]

            name.append(n)
            price.append(p)
            stock.append(s)
            records += 1
            iItem.append(records)

      #-----------------------Options----------------------------------
    for i in range (0,records):                                 
        print(color.BOLD+color.YELLOW+color.UNDERLINE+"{0})".format(i+1)+color.RED+color.BOLD+" {0}:".format(name[i])+color.GREEN+color.BOLD+"${0}\n\n".format(price[i])+color.END)
    #----------------------------------------------------------------

    #entering loop
    loop ='y'


    while loop == 'y':

        choice = choice = int(input(color.UNDERLINE+color.YELLOW+"What would you like to order today?(Please choose from 1-{0}):\n\t".format(records)+color.END))  #records because the amount of records are the amount of rows we have in the csv file
            

        #This will allow the code to see if the choice the customer made was valid and then if it's within the threshold it'll print the item cost and ask how many of that specific item they'd want
        rekon = choice - 1
            

            #it has to be rekon because it's the users choice 1 would be 1 in the CSV file but not the 1 they want so we need to put choice - 1 so that it registers that when they want the first item it's 0 and the second item is 1 in the list

        if choice == iItem[rekon]:

            correction = input(color.YELLOW+"\nYou have selected {0} is that correct?[y/n]\n".format(name[rekon])+color.END)
            correction = correction.lower()

            if correction == 'y':
                print(color.RED+"\nGreat!\n"+color.END)

                quantity = int(input(color.BOLD+color.PURPLE+"\nHow many {0} are you planning on buying?\n\t***PLEASE BE ADVISED EACH {0} COSTS ${1}***\n".format(name[rekon],price[rekon])+color.END))

                #temporary total = quantity * the price of the specific item they want
                tempTotal = quantity * price[rekon]

                correction1 = input(color.YELLOW+"\n\n{0} {1}('s) will be ${2:0.2f} is that ok?\n".format(quantity,name[rekon],tempTotal)+color.END)
                correction1 = correction1.lower()

                if correction1 == 'y':
                    total += tempTotal

                    #set tempTotal to 0 so that it'll reset and show you the price for only the bulk items you're planning on buying and not having it added with every loop

                    tempTotal = 0
                    loop = 'n'
                    
                elif correction1 == 'n':
                    tempTotal = 0
                    print(color.RED+"\n\nplease try again!\n\n"+color.END)
                        
                    
                elif correction1 != 'y' or correction1 !='n':
                    tempTotal = 0
                    loop = 'y'
                
            else:
                print(color.RED+"\n\nERROR\n\n"+color.END)
                loop = 'y'
            
        else: 
            print(color.RED+"\n\nERROR!\n\n"+color.END)
            loop = 'y'



        #exiting loop
        print(color.RED+"\nDo you want to continue shopping?"+color.END)
        loop = input(color.YELLOW+"\n[y/n] : "+color.END)
        loop.lower()

    return total

#---------------------------------------------------------------------------------------


#Main loop

answer = 'y' #while loop answer thingy

while answer == 'y':

    print("\n\n-----------------Welcoming Statment-------------------")
    
    print("Hello welcome to NEIT Black Market what are you looking to buy today.")

    print(color.RED+color.BOLD+"\n\n1. Technology"+color.END)
    print(color.CYAN+color.BOLD+"\n2. Clothing"+color.END)
    print(color.GREEN+color.BOLD+"\n3. Food\n"+color.END)
    print(color.YELLOW+"4.Exit"+color.END)

    q1 = int(input(color.BOLD+color.UNDERLINE+color.YELLOW+"\nInput:"+color.END+color.END+color.END))
    
    if q1 == 1:
        tech()
        
        

    if q1 == 2:
        clothing()

    if q1 == 3:
        food()

    if q1 == 4:
        print("Are you sure you want to checkout?")
        answer1 = input(" \nInput[Y/N]: ")
        answer1.lower()

        if(answer1 == 'y'):
            answer = 'n'

        if(answer1 == 'n'):
            answer = 'y'
    
    elif q1 != 1 and q1 != 2 and q1 != 3 and q1 != 4:
        print("SELECTION NOT AVAILABLE PLEASE TRY AGAIN")
        answer = input(" \nDo You wish to try again?\n\nInput[Y/N]: ")
        answer.lower()
    

#---------------------------------------------------------------------------------------
#Ending code print out goodbye statement 

print(color.RED+"Your total comes out to ${0:0.2f}, your belongings will be ready shortly.\n\nThank you for shopping NEIT Student Black Market \n\nWhere all of your missing belongings go to! \n\nPs.We know where you live. Don't tell anyone about us. \n\nEspecially Ms. Truchon".format(total)+color.END)


#---------------------------------------------------------------------------------------