#Name: Ethan Carrera
#Date: 7/26/2021
#lab: C

#Variable Dictionary: -------------------------------------------
# capR = capacity of a room
# att = Attendee
# hmm = How many more people can attend (will change depending on the numbers)
# answer = if the loop continues or not 
#-----------------------------------------------------------------





#This program will have the user input how big the room is and how many people are attending and then printing out how many more people can attend before it's at max capacity

#________________FUNCTION CODE_________________________

def capacity():
    #A.	A function that asks the user for the maximum capacity of the rooms and returns that value.
    #Use capacity for the name of the function.


    capR = int(input("What is the capacity of the room?\n\t Enter Here: "))

    return capR



def attendees():
    #A function that asks the user for the number of people (attendees)  attending the conference and returns that value. Use attendees for the name of the function.
    att = int(input("\n\nHow many people want to attend this event?\n\t Enter Here:  "))

    return att


def register(capR,att):

    #A function that accepts/is passed the values returned by the    functions capacity and attendees and returns the difference between the room capacity and the attendees. Use register for the name of the function.

    
    if(capR < att):
        hmm = att - capR
        
        print("\nYou have exeeded the limit. \nPlease kick out:[ {0} ] of the attendants".format(hmm))
    
    if(capR > att):
        hmm = capR - att

        print("\nYou still have space. \n You can still invite:\t[ {0} ] attendants.".format(hmm))
    
    elif(capR == att):

        print("\nWOW! You are able to fit everyone perfectly! If you wish to hold more people think about renting a bigger room! ")


def checkings():
    #D.	A function that prompts the user to see if they want to check anymore   rooms. This function should only return if the user selects a lower/  uppercase selects a lower/uppercase y or n.

    answer = input("\nDo you want to check anymore rooms?\n[y/n]: ")

    #remove the case sensitivity!!!!
    answer = answer.lower()

    while answer !='y' and answer != 'n':
        print("ERROR NOT A VALID INPUT BZT BZT")

        answer = input("\n\tDo you want to check anymore rooms?\n[y/n]: ")

        #remove the case sensitivity again!

        answer = answer.lower()

    return answer



#________________MAIN CODE_________________________

#so that the loop can begin
answer = 'y'

while answer == 'y':
    capR = capacity()
    att = attendees()

    c = capR
    a = att

    register(c , a)


    answer = checkings()

print("Thank you have a beautiful day!")