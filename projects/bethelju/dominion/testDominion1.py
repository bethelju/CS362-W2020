# -*- coding: utf-8 -*-
"""
Created on Thurs Jan 16 2020

@author: Justin Bethel
"""

import Dominion
import random
import testUtility
from collections import defaultdict

#Get player names
#Our bug is introduced here, by introducing zero players the game loops endlessly
player_names = []

#number of curses and victory cards
if len(player_names)>2:
    #I changed the number of victory cards here to see if it would be reflected in amount of estate cards
    nV=10
else:
    nV=8
nC = -10 + 10 * len(player_names)

#Define box
box = testUtility.getBoxes(nV)

supply_order = testUtility.setSupplyOrder()

supply = testUtility.setSupply(box, player_names, nV, nC)
print(len(supply["Estate"]))

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.setUpPlayers(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)