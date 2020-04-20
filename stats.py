import sys
import random
import validate_roll

def findSixKind():
    #returns number of rolls required to roll 6 of a kind
    loops = 0
    while True:
        loops = loops + 1
        six_dice = [0,0,0,0,0,0]
        i = 0
        while i < 6:
            six_dice[i] = random.randrange(1,6)
            i = i+1
        r_set=list(set(six_dice))
        if len(r_set)==1: return loops
        else: continue

def findFarkle():
    #returns number of rolls required to roll 6 of a kind
    loops = 0
    
    while True:
        loops = loops + 1
        lengthRoll = random.randrange(1,6)
        some_dice = [0]*lengthRoll
        i = 0
        while i < lengthRoll:
            some_dice[i] = random.randrange(1,6)
            i = i+1
        # r_set=list(set(six_dice))
        # if len(r_set)==1: return loops
        if validate_roll.farkled(some_dice): return loops
        else: continue


mastList = []
i = 0
while i < 100:
    # n = findSixKind()
    n = findFarkle()
    mastList.append(n)
    print n
    i = i+1

print 'ran 100 times'
print 'average: ' + str(sum(mastList)/len(mastList))
print 'max: ' + str(max(mastList))
print 'min: ' + str(min(mastList))
print str(mastList)