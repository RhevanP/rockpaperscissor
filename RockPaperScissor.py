#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:17:51 2020

@author: anthonypascale
"""
import random
import math
from decideChoices import decideChoices
from strongWeak import strongWeak
from userInputCheck import checkingInput
from bestOfCheck import bestOfCheck
from Winnercheck import winnerCheck

#Define variables
#Decide choices
Choices = decideChoices()
#Decide strongest vs weakest
if Choices != "quit" :
    Choices = strongWeak(Choices)
numberOfGames = 0
computerScore = 0
userScore = 0


#Select the type of bestof
if Choices == "quit" :
    print("you left the game")
else :
    while True :
        bestOf = input("What kind of Best Of you want to play ? ")
        bestOf = bestOfCheck(bestOf)
        if bestOf == "quit" :
            break
        elif bestOf > 0 and bestOf%2 != 0:
            break
    
    #play until the bestof is over
    if bestOf != "quit" :
        while numberOfGames < bestOf :
            print("Your score : ", userScore)
            print("Computer score : ", computerScore)
            print("Number of game left to play : ", bestOf-numberOfGames)
            #Computer randomly select the choice
            computerChoice = Choices[random.randint(0,len(Choices)-1)]
            print(computerChoice)
            
            #Check user input
            while True :
                userChoice = input("Paper (1), Rock (2) or Scissor? (3) ")
                if userChoice == "quit" : #quit condition that will allow the user to quit the game if he wants.
                    break
                listResults = checkingInput(userChoice, Choices) #Check if the user input makes sense
                userChoiceChecked = listResults[0]
                if listResults[1] == 1 :
                    break
            
            #Win, loose or egality ? (3,2,1)
            winningSituation = winnerCheck(userChoice, userChoiceChecked, computerChoice, Choices)
            print(winningSituation)
            if winningSituation == 0 or winningSituation == 2 or winningSituation == 3 :
                if winningSituation == 2 :
                    computerScore += 1
                    numberOfGames +=1
                    if(computerScore == math.ceil(bestOf/2)) :
                        break
                elif winningSituation == 3 :
                    userScore += 1
                    numberOfGames += 1
                    if(userScore == math.ceil(bestOf/2)) :
                        break
                else :
                    break
        
        #Displaying the results        
        if userScore > computerScore and userChoice !="quit":
            print("WOUHOUUUU, YOU WOOOON THE GAME")
        elif userChoice == "quit" :
            print("You quitted the game")
        else :
            print("Let's not talk about that...")
    else :
        print("You left the game")
    