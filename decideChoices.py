#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:34:07 2020

@author: anthonypascale
"""

def decideChoices () :
    while True :
        Choices = list()
        input_string = input("Enter a list of 3 elements separated by space or enter 'default' if you want to play normally : ")
        Choices = input_string.split()
        if Choices[0].lower() == "default" :
            ChoicesLowered = ["paper", "rock", "scissor"]
            break
        elif Choices[0] == "quit" :
            ChoicesLowered = Choices[0]
            break
        elif len(Choices) != 3 :
            print("You did not enter 3 elements")
        else :
            ChoicesLowered = [Choices[0].lower(), Choices[1].lower(), Choices[2].lower()]
            break
    return ChoicesLowered