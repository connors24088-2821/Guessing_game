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
    min_name = 2#minimum name so it cant be under it
    max_name = 10
    """This function is to get the user to enter there name and to cheak that they have only entered letters and they it doesnt exede the boundrys of 1 to 10"""
   
    while True:# make a while loop so that if what the user enter is wrong it makes them re enter it
        name = input("Enter your name")#gets the user to enter their name
            
        if not name.isalpha():# makes sure that the name only uses the alphabet
            print("Please only enter letters")
        elif len(name) < max_name and len(name) > min_name: #cheaks if the names are the right lengths and if they are it returns them
            return name # returns name if right lenght
        else:# if the name is not the right lenghts it tells them that
            print("Please make your name bettween 2 and 10 letter")#prints how long there name nees to be


def cheak_age():#calls function
    max_age = 60#gets max_age
    min_age = 10#gets min_age

    while (True):#gets a while true loop
        try:#use try: so that if they enter letters it doesn't work
            age = int(input("Please enter your age"))#get them to enter their age 
            if age >= min_age and age <= max_age:#cheack if the age is right (like if it is inbettween the max and min age vairble)
                return age #if it is bettween min and max age return age
            else:
                print("Please enter your age bettween 10 and 60")#if age isnt bettween min and max age it will print please enter your age bettween 10 and 60

        except ValueError: #  use except valueerror so that if they dont enter an int then it doesnt crash 
            print("Please only enter numbers and whole numbers")#prints and tells them to only enter numbers and whole numbers




#------------main routine----------------------
list_numbers = []
if(__name__=="__main__"):
    # enter a name
    cheak_name() #to cheak there name is right
    # enter age
    cheak_age()
    # make a list of number
    list_maker() # it will make a list of number bettween 1 and 100
    # intro to the game
    #computer rand number
    rand_numbers = random.choice(list_maker())
    cheak_guess()#use a function to check the guess
    # give higher or lower
    # count amount of guesses
    # give the stats how it took to guess