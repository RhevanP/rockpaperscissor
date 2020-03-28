#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 15:04:53 2020

@author: anthonypascale
"""

def bestOfCheck (bestOf) :
    try :
        bestOf = int(bestOf)
        if bestOf > 0 and bestOf%2 != 0 :
            return bestOf
        elif bestOf%2 == 0:
            print("You can have a tie in the end! Choose an uneven number")
            return 0
        else :
            print("Your entry of number is negative, please enter a correct number")
            return 0 
    except :
        if bestOf == "quit" :
            return bestOf
        else :
            print("You did not enter a number")