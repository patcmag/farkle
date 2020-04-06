import sys


def isFourKind(faceCount):
    if faceCount.count(0) == 5 and faceCount.count(4) == 1:
        return True
    else: return False

def isFiveKind(faceCount):
    if faceCount.count(0) == 5 and faceCount.count(5) == 1:
        return True
    else: return False

def isSixKind(faceCount):
    if faceCount.count(0) == 5 and faceCount.count(6) == 1:
        return True
    else: return False

def isThreePairs(faceCount):
    if faceCount.count(0) == 3 and faceCount.count(2) == 3:
        return True
    else: return False

def isTwoTriples(faceCount):
    if faceCount.count(0) == 4 and faceCount.count(3) == 2:
        return True
    else: return False

def isStraight(faceCount):
    if faceCount == [1,1,1,1,1,1]: return True
    else: return False


def isValid(roll):
    print 'roll = ' + str(roll)

    # maybe useful?
    # roll = [int(x) for x in roll if x.isdigit()]
    # types = [type(x) for x in roll]
    
    diceFaces = ['1','2','3','4','5']
    for r in roll:
        if r not in diceFaces:
            # print str(r) + ' removed, not possible.'
            # roll.remove(r)
            # print 'roll = ' + str(roll)
            print 'not a valid roll'
            return False

    #roll will be a list string-format ints - convert to ints
    roll = [int(x) for x in roll if x.isdigit()]

    #count for each dice 'face' submitted for scoring
    faceCount = [roll.count(i) for i in [1,2,3,4,5,6]]
    if sum(faceCount) > 6: 
        print 'not a valid roll'
        return False

    if isFourKind(faceCount):   return True
    if isFiveKind(faceCount):   return True
    if isSixKind(faceCount):    return True
    if isThreePairs(faceCount): return True
    if isTwoTriples(faceCount): return True
    if isStraight(faceCount):   return True

    #counts placed into dictionary dice_dict
    #key = dice face (1-6); value = count of that face
    dice_dict = {}
    i = 1
    for count in faceCount: #create the dictionary
        dice_dict[i] = count
        i = i + 1
    
    for i in [1,2,3,4,5,6]:
        if dice_dict[i] not in [0,3]:  #3 of a kind, N/As
            if dice_dict[i] in [1,2] and i not in [1,5]: #single scoring ones, fives
                print 'not a valid roll'
                return False
        else:
            continue

    return True