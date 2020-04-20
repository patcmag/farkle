import sys
import random

def return_score(roll):
    local_score = 0
    r_set = list(set(roll)) #set is all unique elements; list makes it indexable
    cnt_all_rolls = [roll.count(i) for i in [1,2,3,4,5,6]]

    # 3 DICE  ********************************************************
    # scoring ones and fives but no triple
    if len(roll) < 3 or (len(roll) == 3 and r_set == [1,5]):
        local_score = 100*(roll.count(1)) + 50*(roll.count(5))    
    elif len(roll) == 3:      # scoring a triple
        if r_set[0] == 1: local_score = 750   # (3) ones
        else: local_score = 100*r_set[0]
        
    # 4 DICE ********************************************************
    elif len(roll) == 4:
        if len(r_set) == 1:   #four of a kind
            local_score = 1000
        elif len(r_set) == 2:  
            #if there is a triple, there is (1) three in cnt_all_rolls
            #(add 1 to align with dice face values)
            if 3 in cnt_all_rolls:
                triple = cnt_all_rolls.index(3) + 1
                if triple == 1: local_score = 750
                else: local_score = 100*triple
                #last die is (1) or (5)
                remainder = cnt_all_rolls.index(1) + 1
                if remainder == 1:   local_score = local_score + 100
                elif remainder == 5: local_score = local_score + 50
            else:   
                local_score = 300   # [1,5,1,5] 
        else: print 'something went wrong'
            
    # 5 DICE ********************************************************
        # 5 of any number
        # triple plus (2) one or five
        # four of a kind plus (1) one or five
    elif len(roll) == 5:
        if len(r_set) == 1:   #five of a kind
            local_score = 2000
        elif len(r_set) in [2,3]:  #triple plus (2) add'l one/five       
            cnt_all_rolls = [roll.count(i) for i in [1,2,3,4,5,6]]
            #this only occurs on four of a kind plus (1) one or five
            if 4 in cnt_all_rolls:
                #add 1 to align with dice face values
                if   cnt_all_rolls.index(1)+1 == 1: local_score = 1100
                elif cnt_all_rolls.index(1)+1 == 5: local_score = 1050
                else: print 'something went wrong'
            else:
                #there should only be (1) three in this list
                #add 1 to align with dice face values
                triple = cnt_all_rolls.index(3) + 1
                if triple == 1: local_score = 750
                else: local_score = 100*triple

                #the remainder
                if 2 in cnt_all_rolls:                             # (2) ones or (2) fives
                    twoSameDiceRemainder = cnt_all_rolls.index(2) + 1
                    if twoSameDiceRemainder == 1:   local_score = local_score + 200
                    elif twoSameDiceRemainder == 5: local_score = local_score + 100
                elif cnt_all_rolls[0]==1 and cnt_all_rolls[4]==1:  # (1) each one and five
                    local_score = local_score + 150
                else: print 'something went wrong'        

    # 6 DICE ********************************************************
        # 6 of any number
        # two triples
        # three pairs
        # one thru six straight

        #3,4,5 of a kind plus remainder of ones and fives
    elif len(roll) == 6:
        if len(r_set) == 1: local_score = 3000                                  #six of a kind
        elif len(r_set) == 2 and 3 in cnt_all_rolls: local_score = 2500         #two triples
        elif len(r_set) == 3 and max(cnt_all_rolls) == 2: local_score = 1500    #three pairs
        elif 3 in cnt_all_rolls:
            if cnt_all_rolls[0] == 3: local_score = 750
            else: local_score = (cnt_all_rolls.index(3)+1)*100
            local_score = local_score + (250 if cnt_all_rolls[0] == 2 else 200)

        elif 4 in cnt_all_rolls:
            if len(r_set) == 2:          # 4 kind + (2) ones or (2) fives
                local_score = 1000 + (200 if cnt_all_rolls[0] == 2 else 100)
            else: local_score = 1150     # 4 kind + (1) one and (1) 5
    
        elif 5 in cnt_all_rolls:         # 5 kind + (1) one/five
            local_score = 2000 + (100 if cnt_all_rolls[0] == 1 else 50)

        elif len(r_set) == 6: local_score = 1500   # 1-6 straight
        else: print 'something went wrong'

    #these statements shouldn't be necessary if we have a data validation function
    #which makes sure the length of the scored roll is correct
    else: print 'something went wrong'

    return local_score