'''
    author: Connor Sinclair
    date: 19/03/26
    version: 1
    description: This is a guessing game where you guess a number bettween 1 t0 100

'''

#------------librarirs----------------------
import random

#------------functions----------------------
def list_maker():
    """ This function create a list of numbers from 1-100 and stores it in a list. @p -none. @r -return type list of ints"""
    rand_numbers = []
    # create a list of numbers
    for i in range(1,101):
        rand_numbers.append(i)
    return rand_numbers


def cheak_name():
    min_name = 2
    max_name = 10
    """This function is to get the user to enter there name and to cheak that they have only entered letters and they it doesnt exede the boundrys of 1 to 10"""
   
    while True:# make a while loop so that if what the user enter is wrong it makes them re enter it
        name = input("Enter your name")#gets the user to enter their name
            
        if not name.isalpha():# makes sure that the name only uses the alphabet
            print("Please only enter letters")
        elif len(name) < max_name and len(name) > min_name: #cheaks if the names are the right lengths and if they are it returns them
            return name # returns name if right lenght
        else:# if the name is not the right lenghts it tells them that
            print("Please make your name bettween 2 and 10 letter")
#------------main routine----------------------
list_numbers = []
if(__name__=="__main__"):
    # enter a name
    cheak_name() #to cheak there name is right
    # enter age
    # make a list of number
    list_maker() # it will make a list of number bettween 1 and 100
    # intro to the game
    #computer rand number
    rand_numbers = random.choice(list_maker())
    # ask user to guess 
    # give higher or lower
    # count amount of guesses
    # give the stats how it took to guess