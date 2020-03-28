#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 12:31:02 2020

@author: anthonypascale
"""

#Check user Input
def checkingInput (userChoice, Choices) :
    try :
        userChoiceN = int(userChoice)-1
        if userChoiceN < 0 :
            print('Your value was negative, you can only enter a positive one. Do it again')
            return[0,0]
        elif userChoiceN > len(Choices)-1 :
            print('Your value was way too high, enter a correct number.')
            return[0,0]
        else :
            userChoice = Choices[userChoiceN]
            return [userChoice,1]
    except :
        userChoice = userChoice.lower()
        if (userChoice in Choices) == False:
            print('Your entry was not in the possibilities, do it again')
            return[0,0]
        elif (userChoice in Choices) == True:
            return [userChoice,1]