import sys
import random

def return_score(roll):
    local_score = 0
    r_set = list(set(roll)) #set is all unique elements; list makes it indexable

    # scoring ones and fives, but not a triple
    if len(roll) < 3 or (len(roll) == 3 and r_set == [1,5]):
        local_score = 100*(roll.count(1)) + 50*(roll.count(5))
    
    # scoring a triple
    elif len(roll) == 3: 
        if r_set[0] == 1:     #(3) ones
            local_score = 750
        else:
            local_score = 100*r_set[0]
        
    # scoring exactly 4 dice
    elif len(roll) == 4:
        if len(r_set) == 1:   #four of a kind
            local_score = 1000
        elif len(r_set) == 2: #triple plus (1) one or five 
            cnt_all_rolls = [roll.count(i) for i in [1,2,3,4,5,6]]
            
            #there should only be (1) three in this list
            #add 1 to align with dice face values
            triple = cnt_all_rolls.index(3) + 1
            if triple == 1: local_score = 750
            else: local_score = 100*triple

            #the remainder is the one or five that is part of this 4-dice roll
            #along with a triple
            remainder = cnt_all_rolls.index(1) + 1
            if remainder == 1:   local_score = local_score + 100
            elif remainder == 5: local_score = local_score + 50
            
            else: print 'something went wrong'

    # scoring exactly 5 dice can be
        # 5 of any number
        # triple plus (2) one or five

    # scoring exactly 6 dice can be
        # 6 of any number
        # two triples
        # three pairs
        # one thru six straight

    # else:
    #     value_counts = {}
    #     for i in [1,2,3,4,5,6]:
    #         score_dict[i] = roll.count(i) #[key/value] = [dice value/#times value appears]

    
    #else: #this is for 4,5,6 of a kinds, triples plus 1s or 5s, straights, 2-3s, 3-2s
    return local_score