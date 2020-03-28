#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:46:51 2020

@author: anthonypascale
"""

def strongWeak(Choices) :
    print ("In the current state ", Choices[0], " beats ", Choices[1], " who beats ", Choices [2], " who beats ", Choices[0])
    while True :
        userAnswer = input("Are you happy with the current situation of winning/loosing ? ")
        if userAnswer.lower() == "yes" or userAnswer.lower() == "y" :
            newChoices = Choices
            break
        elif userAnswer.lower() == "no" or userAnswer.lower() == "n":
            newChoices = [Choices[2], Choices[1], Choices[0]]
            print ("In the current state ", newChoices[0], " beats ", newChoices[1], " who beats ", newChoices [2], " who beats ", newChoices[0])
            Choices = newChoices
        elif userAnswer.lower() == "quit" :
            newChoices = "quit"
            break
        else :
            print("You did NOT answer with yes or y or no or n. Please try again.")
    return newChoices

#IDEAS
#Randomise the order of the first list given
#Make a check about the yes or no input