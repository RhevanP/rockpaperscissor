#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 11:02:48 2020

@author: anthonypascale
"""
def winnerCheck (userChoice, userChoiceChecked, computerChoice, Choices) :
    if userChoice == "quit" : #Allow user to quit the game
        return 0
    elif userChoiceChecked == computerChoice : #text vs text
        print ("It's a tie! Both of you choosed ", computerChoice)
        return 1
    elif Choices.index(userChoiceChecked) == len(Choices)-1 and Choices.index(computerChoice) == 0 :
        print("You win this round! You choosed ", userChoiceChecked, " which beats ", computerChoice)
        return 3
    elif Choices.index(userChoiceChecked) > Choices.index(computerChoice) :
        print("Computer wins this round! He choosed ", computerChoice, " which beats ", userChoiceChecked) #Compare the text
        return 2
    elif Choices.index(computerChoice) == (len(Choices)-1) and Choices.index(userChoiceChecked) == 0 :
        print("Computer wins this round! He choosed ", computerChoice, " which beats ", userChoiceChecked) #Compare the text
        return 2
    else :
        print("You win this round! You choosed ", userChoiceChecked, " which beats ", computerChoice)
        return 3