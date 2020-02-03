# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 09:46:11 2018

@author: andrew.mcdonald

This pin generator program allows the user to chose between generating a simple 4 digit pin
or a custom length pin number.
"""

#importing the random library
import random
    
def pingenerator_simple():
    #This function creates 4 separate numbers between 0 and 9 which can be joined together
    #The reason for 4 separate values is to include leading 0s - When converted to a string this could
    #be achieved by using .zfill
    
    pin1 = random.randint(0,9)
    pin2 = random.randint(0,9)
    pin3 = random.randint(0,9)
    pin4 = random.randint(0,9)
    
    #Join together the individual variables
    fin_pin = f'{pin1}{pin2}{pin3}{pin4}'
    
    return fin_pin


def pingenerator_digits():
    #This function allows the user to specify the number of digits for the pin number
    
    #set the counter and empty list
    count = 0
    pin = []
    
    #ask the user for the number of digits
    pindigits = int(input('How many digits would you like for your new pin?:   '))
    
    #append to the list whilst the count is less than the number of required digits
    while count < pindigits:
        pin.append(random.randint(0,9))
        count += 1
        
    #join together the final list
    fin_pin = (''.join(map(str,(pin))))
            
    return fin_pin


generate = True
while generate is True:

    choice = 0
    while not choice:
        #Try Except used to catch non-integers and values outside of choice
        try:
            choice = int(input('Choose a pin generator using either 1 or 2: Four-Digits (1) or Custom Length (2):  '))
            if choice not in (1,2):
                raise ValueError
        except ValueError:
            choice = 0
            print('Invalid Selection! Please enter 1 or 2')
    
    if choice == 1:
        print(f'Your simple 4-digit pin is: {pingenerator_simple()}')
    elif choice == 2:
        print(f'Your custom length pin is: {pingenerator_digits()}')
    
    #check to see if the user would like to run the generator again
    runagain = input('Would you like to generate another pin number? Enter Y or N:   ')
    
    #if any value other than y/Yes/yes is entered then end the program
    if runagain.lower()[0] == 'y':
        generate = True
    else:
        generate = False
