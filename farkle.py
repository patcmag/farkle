#!/usr/bin/python

import sys
import random
import return_score
import validate_roll
import subprocess as sp


# MAIN GAME    

print 'welcome to farkle v1\n'

players = ['p1', 'p2', 'p3']
playerScores = {'p1':0, 'p2':0, 'p3':0}

while True: #game runs until CTRL-C, needs work
    for player in players: #PLAYER TURN, cycles through p1,p2,p3
        
        turnContinues = True
        activeDice = 6
        turn_score = 0

        while turnContinues:
            # print player + ' turn score: ' + str(turn_score)
            print 'BANKED SCORES'
            for p in players: print p + ": " + str(playerScores[p]) #print all players' current scores
            try:
                input( '\nhit enter to roll dice\t\t' + player + ' score for this turn: ' + str(turn_score))
            except SyntaxError:
                pass

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
        
            # debug troublesome rolls
            # activeDice = 4
            # dice_dict = {'1':3,'2':3,'3':4,'4':5}

            #test if Farkled
            if validate_roll.farkled([dice_dict[str(j)] for j in range(1,activeDice+1)]):
                print '* * * F A R K L E * * *'
                turnContinues = False
                turn_score = 0
                continue # back to while True

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
            turn_score = turn_score + current_score
            print 'score for these dice: ' + str(current_score)
            print 'current score was calculated from these values:   ' + str(scoreList)

            activeDice = len(turn_dice_dict)
            if activeDice == 0: 
                print 'you get a fresh set of dice'
                activeDice = 6
                # turn_score = turn_score + current_score
                try:
                    input( '\nHIT ENTER TO CONTINUE')
                except SyntaxError: 
                    pass
                sp.call('clear',shell=True)
                continue
            else:
                print 'you have ' + str(activeDice) + ' remaining dice'

            waitingForValidChoice = True
            choice = ''
            while waitingForValidChoice:
                choice = raw_input('\n\n' + player + ', continue to roll?\n(yes/no)\t').strip()
                if choice not in ['yes','no']: 
                    print 'not a valid response'
                    continue
                else: 
                    waitingForValidChoice = False
            if choice == 'yes' : 
                sp.call('clear',shell=True)
                continue
            elif choice == 'no': #bank score
                playerScores[player] = playerScores[player] + turn_score
                turnContinues = False

        print player + ', your turn score is:\t\t' + str(turn_score) 
        print player + ', your total score is:\t' + str(playerScores[player]) 
        #print '\nyour score will be calculated from ' + str(return_score(score_list)) + ' separate values'

        try:
            input( '\nHIT ENTER TO CONTINUE')
        except SyntaxError:
            pass
        
        sp.call('clear',shell=True)

