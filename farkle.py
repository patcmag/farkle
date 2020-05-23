#!/usr/bin/python

import sys
import random
import return_score
import validate_roll
import gui
import dieObject
import subprocess as sp
import tkinter as tk
from tkinter import * #Tk, Button, Label, BOTTOM, TOP, LEFT, CENTER, Canvas

root = Tk()

#outer GUI with areas for dice and scoring
gameWindow = Frame(root,height=600,width=650)
gameWindow.grid(row=0,column=0,padx=10,pady=2)

#area where dice are visualized
playArea = Frame(gameWindow,height=500,width=550)
playArea.grid(row=0,column=0,padx=40,pady=10)

#create dice canvas
#wrap in function to clear and re-create during gameplay
def createCanvas():
    c = Canvas(playArea,height=500,width=550)
    c.grid(row=0,column=0,padx=10,pady=2)
    c.create_rectangle(3,3,550,500) #show boarder of playArea
    return c
canvas = createCanvas()

gui_p1_score = IntVar(0)
gui_p2_score = IntVar(0)
gui_p3_score = IntVar(0)
gui_player_labels = ['Player 1:\t','Player 2:\t','Player 3:\t']
gui_scores=[gui_p1_score,gui_p2_score,gui_p3_score]

i=0
for p in gui_player_labels:
    tk.Label(gameWindow,text=p).grid(row=i+1,column=0)
    tk.Label(gameWindow,textvariable=str(gui_scores[i])).grid(row=i+1,column=1)
    i=i+1

gui_current_score = IntVar(0)
tk.Label(gameWindow,text='Most recent roll scored: ').grid(row=4,column=0)
tk.Label(gameWindow,textvariable=str(gui_current_score)).grid(row=4,column=1)

gui_turn_score = IntVar(0)
tk.Label(gameWindow,text='Current score for this turn: ').grid(row=5,column=0)
tk.Label(gameWindow,textvariable=str(gui_turn_score)).grid(row=5,column=1)

# game logic does not run with this here - move to end of code?
# root.mainloop()  #https://stackoverflow.com/questions/8683217/when-do-i-need-to-call-mainloop-in-a-tkinter-application




#=====================MAIN GAME=====================

def userInput(promptStr):
    u_in = raw_input(promptStr)
    try:
        if u_in.strip() in ['q','Q']: quit()
    except SyntaxError: pass
    return u_in

#coordinates for the dice in GUI
rec1 = [x+100 for x in [20,10,100,90]]
rec2 = [x+100 for x in [20,100,100,180]]
rec3 = [x+100 for x in [20,190,100,270]]
rec4 = [x+100 for x in [170,10,250,90]]
rec5 = [x+100 for x in [170,100,250,180]]
rec6 = [x+100 for x in [170,190,250,270]]
recList = [rec1,rec2,rec3,rec4,rec5,rec6]

players = ['p1', 'p2', 'p3']
playerScores = {'p1':0, 'p2':0, 'p3':0}
gui_playerScores = {'p1':gui_p1_score, 'p2':gui_p2_score, 'p3':gui_p3_score}
inheritingRoll = False

print 'welcome to farkle v2\n'
while True:                 #NEEDS WORK - EXIT COMMAND
    for player in players:  #PLAYER TURN, cycles through p1,p2,p3
        turnContinues = True

        #this resets to 6 dice and 0 turn points if previous player farkles 
        #OR if current player decides to start over with fresh dice
        if inheritingRoll==False: 
            activeDice = 6
            current_score = 0
            gui_current_score.set(0)
            turn_score = 0
            gui_turn_score.set(0)

        while turnContinues:
            print 'BANKED SCORES'
            for p in players: print p + ": " + str(playerScores[p]) #print all players' current scores
            # print player + ', your turn score is:\t\t' + str(turn_score) 
            # print player + ', your total score is:\t' + str(playerScores[player]) 
            userInput('Hit enter to roll dice\t\t\tQ to quit\n')            
            dice = [0]*activeDice
            dice_dict = {}

            i = 1
            print 'DIE\tROLL'
            for d in dice:
                roll = random.randrange(1,7)
                dice_dict[str(i)] = roll
                print '[d'+str(i)+']\t'+str(roll)
                i = i+1

            #values of dice just rolled
            current_roll = [dice_dict[str(j)] for j in range(1,activeDice+1)]
            #IDs (1-6) of dice just rolled
            active_dice_IDs = [str(id) for id in range(1,activeDice+1)]

            # debug troublesome rolls
            # current_roll = [1,2,3,4,5,6]
            # active_dice_IDs = ['1','2','3','4','5','6']

            #visualize dice in GUI
            dieObject_list = [] #holds refs to GUI dice objects
            i=0
            for id in active_dice_IDs:
                #create Die() instance and add to the dieObject_list
                dieObject_list.append(dieObject.Die(canvas, id, dice_dict[id], *recList[i]))
                i=i+1
            
            #test and end turn if farkled
            if validate_roll.farkled(current_roll):
                print '* * * F A R K L E * * *'
                userInput('\nHit enter to continue\t\t\tQ to quit\n')
                #clear GUI 
                canvas.destroy()
                canvas = createCanvas()

                #reset relevent vars
                turnContinues = False
                inheritingRoll = False
                turn_score = 0
                # continue # back to while True
                break
            
            waitingForValidDice = True
            while waitingForValidDice:
                userInput('\n' + player + ', choose dice to keep.\nPress ENTER to continue.\t\t\tQ to quit\n\n')
                
                dice_to_keep = []
                for d in dieObject_list:
                    if d.get_selected_status() == True: dice_to_keep.append(d.get_dieID())

                #create list of rolled values for this roll
                #to be used to tabulate score for this roll
                scoreList = [dice_dict[die] for die in dice_to_keep] 
                scoreList_IsValid = validate_roll.isValid([str(s) for s in scoreList])
                if scoreList_IsValid == False:
                    print 'Not valid, choose new dice to keep.'
                    continue #back to while waitingForValidDice
                else: waitingForValidDice = False #escape from nested while loop

            turn_dice_dict = dice_dict
            print '\nYou chose\n'
            for die in dice_to_keep:
                print '[d'+str(die)+']\t'+str(dice_dict[die])
                del turn_dice_dict[die] #reduce available dice to roll for this turn
            
            #update (GUI) scoring vars
            current_score = return_score.return_score(scoreList)
            gui_current_score.set(current_score)
            turn_score = turn_score + current_score
            gui_turn_score.set(turn_score)
            # print 'score for these dice: ' + str(current_score)
            # print 'current score was calculated from these values:   ' + str(scoreList)

            activeDice = len(turn_dice_dict)
            if activeDice == 0: 
                print 'You get a fresh set of dice - SWEET.'
                activeDice = 6
                userInput('\nHit enter to continue\t\t\tQ to quit\n')
                sp.call('clear',shell=True)
                #clear GUI
                canvas.destroy()
                canvas = createCanvas()
                continue
            # else: print 'you have ' + str(activeDice) + ' remaining dice'

            waitingForValidChoice = True
            choice = ''
            while waitingForValidChoice:
                choice = userInput('\n' + player + ', continue to roll?\n(yes/no)\t')
                if choice not in ['yes','no']: 
                    print 'not a valid response'
                    continue
                else: waitingForValidChoice = False

            if choice == 'yes' : 
                sp.call('clear',shell=True)
                #clear GUI
                canvas.destroy()
                canvas = createCanvas()
                continue

            elif choice == 'no': #bank score, pass roll to next player
                playerScores[player] = playerScores[player] + turn_score
                gui_playerScores[player].set(playerScores[player])
                turnContinues = False
        
                waitingForValidChoice = True
                choice = ''
                while waitingForValidChoice:
                    choice = userInput('\nNext player, do you want to keep this score?\n(yes/no)\t')
                    if choice not in ['yes','no']: 
                        print 'not a valid response'
                        continue
                    else: waitingForValidChoice = False

                if choice == 'yes' : #next player starts turn with current player's score
                    inheritingRoll = True
                    sp.call('clear',shell=True)
                    #clear GUI
                    canvas.destroy()
                    canvas = createCanvas()
                    continue
                
                elif choice == 'no': #next player starts with fresh dice
                    turnContinues = False
                    inheritingRoll = False    
                    userInput('\nHit enter to continue\t\t\tQ to quit\n')
                    sp.call('clear',shell=True)
                    #clear GUI
                    canvas.destroy()
                    canvas = createCanvas()

