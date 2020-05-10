#!/usr/bin/python

import sys
import random
import return_score
import validate_roll
import gui
import subprocess as sp
import tkinter as tk
from tkinter import * #Tk, Button, Label, BOTTOM, TOP, LEFT, CENTER, Canvas

root = Tk()
# welcomeLabel = Label(root, font = ('Helvetica',16,'bold'), foreground = 'black',
#                     background = 'white', padx=25,pady=10, text='welcome to farkle v3')
# welcomeLabel.pack(side=TOP)

gui_p1_score = IntVar()
gui_p1_score.set(0)
gui_p2_score = IntVar()
gui_p2_score.set(0)
gui_p3_score = IntVar()
gui_p3_score.set(0)

gui_player_labels = ['Player 1:\t','Player 2:\t','Player 3:\t']
gui_scores=[gui_p1_score,gui_p2_score,gui_p3_score]

i=0
for p in gui_player_labels:
    tk.Label(text=p).grid(row=i,column=0)
    tk.Label(textvariable=str(gui_scores[i])).grid(row=i,column=1)
    i=i+1

gui_current_score = IntVar()
gui_current_score.set(0)
tk.Label(text='Most recent roll scored: ').grid(row=3,column=0)
tk.Label(textvariable=str(gui_current_score)).grid(row=3,column=1)

gui_turn_score = IntVar()
gui_turn_score.set(0)
tk.Label(text='Current score for this turn: ').grid(row=4,column=0)
tk.Label(textvariable=str(gui_turn_score)).grid(row=4,column=1)

def startGame():
    clickToPlay.destroy()
    var.set(1)

# var = tk.IntVar()
# clickToPlay = Button(root,text='startGame', command=lambda: var.set(1),padx=100,pady=150)
# clickToPlay.pack(side=BOTTOM)
# # root.mainloop()  #https://stackoverflow.com/questions/8683217/when-do-i-need-to-call-mainloop-in-a-tkinter-application
# clickToPlay.wait_variable(var)
# clickToPlay.destroy()

canvas = Canvas(root,height=500,width=550)
canvas.create_rectangle(3,3,550,500) 
# canvas.pack(side=TOP)
canvas.grid(row=5,column=3)

# var = tk.IntVar()
# clickToPlay = Button(root,text='Start game', command=startGame,padx=50,pady=25)
# # clickToPlay.pack()
# clickToPlay.place(relx=.5, rely=.5, anchor="center")
# clickToPlay.wait_variable(var)
# clickToPlay.delete()
# root.mainloop()  #https://stackoverflow.com/questions/8683217/when-do-i-need-to-call-mainloop-in-a-tkinter-application


rec1 = [x+100 for x in [20,10,100,90]]
rec2 = [x+100 for x in [20,100,100,180]]
rec3 = [x+100 for x in [20,190,100,270]]
rec4 = [x+100 for x in [170,10,250,90]]
rec5 = [x+100 for x in [170,100,250,180]]
rec6 = [x+100 for x in [170,190,250,270]]
recList = [rec1,rec2,rec3,rec4,rec5,rec6]
# root.mainloop()


print 'welcome to farkle v2\n'
#=====================MAIN GAME=====================

players = ['p1', 'p2', 'p3']
playerScores = {'p1':0, 'p2':0, 'p3':0}
gui_playerScores = {'p1':gui_p1_score, 'p2':gui_p2_score, 'p3':gui_p3_score}

inheritingRoll = False
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
            # print player + ' turn score: ' + str(turn_score)
            print 'BANKED SCORES'
            for p in players: print p + ": " + str(playerScores[p]) #print all players' current scores
            print player + ', your turn score is:\t\t' + str(turn_score) 
            print player + ', your total score is:\t' + str(playerScores[player]) 
            try: raw_input( '\nhit enter to roll dice\t\t' + player + ' score for this turn: ' + str(turn_score))
            except SyntaxError: pass
            print '\n\ndice rollin...\n\n'
            dice = [0]*activeDice
            dice_dict = {}

            i = 1
            print 'DIE\tROLL'
            for die in dice:
                roll = random.randrange(1,6)
                dice_dict[str(i)] = roll
                print '[d'+str(i)+']\t'+str(roll)
                i = i+1

            #values of dice just rolled
            current_roll = [dice_dict[str(j)] for j in range(1,activeDice+1)]
            drawnDice = []  #hold refs to rectangles to delete after turn
            drawnDots = []  #hold refs to ovals to delete after turn

            # debug troublesome rolls
            # activeDice = 4
            # dice_dict = {'1':3,'2':3,'3':4,'4':5}

            #visualize dice in GUI
            i = 0
            for die in current_roll:
                # print 'die ' + str(die)
                drawnDice.append(canvas.create_rectangle(*recList[i]))
                # print 'rec ' + str(recList[i])
                dotCoords = gui.getDieDotCoords(die, recList[i])
                # print 'dotCoords ' + str(dotCoords)
                if die==1: 
                    drawnDots.append(canvas.create_oval(dotCoords,fill="black"))
                else:
                    for dot in dotCoords:
                        # print 'dot ' + str(dot)
                        drawnDots.append(canvas.create_oval(dot,fill="black"))
                i=i+1
            # canvas.pack(side=TOP)

            #test and end turn if farkled
            if validate_roll.farkled(current_roll):#[dice_dict[str(j)] for j in range(1,activeDice+1)]):
                print '* * * F A R K L E * * *'
                try: raw_input( '\nHIT ENTER TO CONTINUE')
                except SyntaxError: pass
                #clear GUI dice / relevent vars 
                for rectangle in drawnDice: canvas.delete(rectangle)
                for oval in drawnDots: canvas.delete(oval)
                turnContinues = False
                inheritingRoll = False
                turn_score = 0
                # continue # back to while True
                break
            
            waitingForValidDice = True
            while waitingForValidDice:
                dice_keep = raw_input('\n\n' + player + ', which dice will you keep? \n(separate by spaces)\t').strip()
                dk = dice_keep.split(' ')
                #create list of rolled values for this roll
                #to be used to tabulate score for this roll
                scoreList = [dice_dict[die] for die in dk] 
                scoreList_IsValid = validate_roll.isValid([str(s) for s in scoreList])
                if scoreList_IsValid == False:
                    print 'not valid, choose new dice to keep'
                    continue #back to while waitingForValidDice
                else: waitingForValidDice = False #escape from nested while loop

            turn_dice_dict = dice_dict
            print '\nyou chose\n'
            for die in dk:
                print '[d'+str(die)+']\t'+str(dice_dict[die])
                del turn_dice_dict[die] #reduce available dice to roll for this turn
            
            current_score = return_score.return_score(scoreList)
            gui_current_score.set(current_score)

            turn_score = turn_score + current_score
            gui_turn_score.set(turn_score)

            print 'score for these dice: ' + str(current_score)
            print 'current score was calculated from these values:   ' + str(scoreList)

            activeDice = len(turn_dice_dict)
            if activeDice == 0: 
                print 'you get a fresh set of dice'
                activeDice = 6
                try: raw_input( '\nHIT ENTER TO CONTINUE')
                except SyntaxError: pass
                sp.call('clear',shell=True)
                #clear GUI
                for rectangle in drawnDice: canvas.delete(rectangle)
                for oval in drawnDots: canvas.delete(oval)
                continue
            else: print 'you have ' + str(activeDice) + ' remaining dice'

            waitingForValidChoice = True
            choice = ''
            while waitingForValidChoice:
                choice = raw_input('\n\n' + player + ', continue to roll?\n(yes/no)\t').strip()
                if choice not in ['yes','no']: 
                    print 'not a valid response'
                    continue
                else: waitingForValidChoice = False

            if choice == 'yes' : 
                sp.call('clear',shell=True)
                #clear GUI
                for rectangle in drawnDice: canvas.delete(rectangle)
                for oval in drawnDots: canvas.delete(oval)
                continue
            elif choice == 'no': #bank score, pass roll to next player
                playerScores[player] = playerScores[player] + turn_score
                gui_playerScores[player].set(playerScores[player])
                turnContinues = False
        
                waitingForValidChoice = True
                choice = ''
                while waitingForValidChoice:
                    choice = raw_input('\n\nnext player, do you want to keep this score?\n(yes/no)\t').strip()
                    if choice not in ['yes','no']: 
                        print 'not a valid response'
                        continue
                    else: waitingForValidChoice = False

                if choice == 'yes' : #next player starts turn with current player's score
                    inheritingRoll = True
                    sp.call('clear',shell=True)
                    #clear GUI
                    for rectangle in drawnDice: canvas.delete(rectangle)
                    for oval in drawnDots: canvas.delete(oval)
                    continue
                
                elif choice == 'no': #next player starts with fresh dice
                    turnContinues = False
                    inheritingRoll = False
                    try: raw_input( '\nHIT ENTER TO CONTINUE')
                    except SyntaxError: pass         
                    sp.call('clear',shell=True)
                    #clear GUI
                    for rectangle in drawnDice: canvas.delete(rectangle)
                    for oval in drawnDots: canvas.delete(oval)

