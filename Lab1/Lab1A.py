#Name: Ethan Carrera
#Date: 7/25/2021
#Lab: A

#Variable Dictionary: 
# capR = capacity of a room
# att = Attendee
# hmm = How many more people can attend (will change depending on the numbers)
# answer = if the loop continues or not 


#This program will have the user input how big the room is and how many people are attending and then printing out how many more people can attend before it's at max capacity

#so that the loop can begin
answer = 'y'

#Some variables I want to declare first
capR = 0 #capacity of room
att = 0 #number of those attending

while(answer=='y'):
    capR = int(input("What is the capacity of the room?\n\t Enter Here: "))
    
    att = int(input("\n\nHow many people want to attend this event?\n\t Enter Here:  "))


    #have it so that depending on which one is greater than the other it'll do the math differently so it doesn't turn into a negative

    if(capR < att):
        hmm = att - capR
        
        print("\nYou have exeeded the limit. \nPlease kick out:[ {0} ] of the attendants".format(hmm))
    
    if(capR > att):
        hmm = capR - att

        print("\nYou still have space. \n You can still invite:\t[ {0} ] attendants.".format(hmm))
    
    elif(capR==att):

        print("\nWOW! You are able to fit everyone perfectly! If you wish to hold more people think about renting a bigger room! ")
    
    answer = input("\nDo you want to check anymore rooms?\n[y/n]: ")
    answer = answer.lower()


print("Thank you, have a nice day!")


#  .-"""-.
# /* * * *\
#:_.-:`:-._;
#    (_)
# \|/(_)\|/   ---------------- ETHAN S. CARRERA