#!/usr/bin/python

import sys
import random
import return_score
import validate_roll

# MAIN GAME    

print 'welcome to farkle v1\n'
while True:
    # this doesn't work
    # usr_in = input( '\nhit enter to roll dice\nq to exit\t')
    # if usr_in == 'q': sys.exit
    # elif len(usr_in)>0: break
    # else: continue 

    try:
        input( '\nhit enter to roll dice\t')
    except SyntaxError:
        pass
    

    print '\n\ndice rollin...\n\n'

    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0
    d6 = 0

    six_dice = [d1,d2,d3,d4,d5,d6]
    dice_dict = {}
    #dice_collection = {1:d1,2:d2,3:d3,4:d4,5:d5,6:d6}

    i = 1
    print 'DIE\tROLL'
    for die in six_dice:
        roll = random.randrange(1,6)
        dice_dict[str(i)] = roll
        print '[d'+str(i)+']\t'+str(roll)
        i = i+1

    dice_keep = raw_input('\n\nwhich dice will you keep? \n(separate by spaces)\t').strip()
    dk = dice_keep.split(' ')

    #create list of rolled values for this roll
    #to be used to tabulate score for this roll
    scoreList = [dice_dict[die] for die in dk] 

    scoreList_IsValid = validate_roll.isValid([str(s) for s in scoreList])
    if scoreList_IsValid == False:
        print 'choose new dice to keep'

    #this is the ID of the die, not the roll/value
    # available_dice_id = [str(x) for x in [1,2,3,4,5,6]]

    # #data validation - input
    # for die in dk:
    #     if die in available_dice_id:
    #         continue
    #     else:
    #         print 'not a possible roll'

    #need more data validation
    #rolls must be a 1s, 5s, 3 of a kind [and other special rolls]
    #another function validate_choice()

    turn_dice_dict = dice_dict
    score = 0


                    
    print '\nyou chose\n'
    for die in dk:
        print '[d'+str(die)+']\t'+str(dice_dict[die])
        del turn_dice_dict[die] #reduce available dice to roll for this turn
    
    print '\nyou have ' + str(len(turn_dice_dict)) + ' remaining dice'
    print '\nyour score will be calculated from these values:   ' + str(scoreList)
    print '\nyour score is:\t' + str(return_score.return_score(scoreList)) 
    #print '\nyour score will be calculated from ' + str(return_score(score_list)) + ' separate values'



