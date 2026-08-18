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

#------------main routine----------------------
list_numbers = []
if(__name__=="__main__"):
    # enter a name
    # enter age
    # make a list of number
    list_maker()# it will make a list of number bettween 1 and 100
    # intro to the game
    #computer rand number
    rand_nu, = random.choice()
    # ask user to guess 
    # give higher or lower
    # count amount of guesses
    # give the stats how it took to guess