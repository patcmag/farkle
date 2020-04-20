#!/usr/bin/python

import sys
import random
import validate_roll

#valid rolls
x1 = [4,4,4] #400
x2 = [1,1,1] #750
x3 = [1,1,5] #250
x4 = [1,5] #150
x5 = [5,5] #100
x6 = [1,1,5,5,6,6] #1500
x7 = [1,2,3,4,5,6] #1500
x8 = [1] #100
x9 = [5] #50
x10 = [5,5,5,1] #600
x11 = [1,5,1,5] #300

x12 = [2,2,3,4,5,6]
x13 = [2,2,3,3,6,6]

#farkles
x14 = [4,2,6]
x15 = [6,6,2,3]
x16 = [3,4,6,2,2]
x17 = [3,3]
x18 = [4]

#valid
x19 = [3,3,4,5]

rolls = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19]

correct_farkled = [False,False,False,False,False,False,False,False,False,False,
                    False,False,False,
                        True,True,True,True,True,
                            False]

#isolate an element, for debugging
# t = 16
# rolls = rolls[t-1:t]
# correct_farkled = correct_farkled[t-1:t]

#tests
i=0
failedFarkled = 0
for r in rolls:
    farkled_result = validate_roll.farkled(r)
    print str(r)
    print 'Actually farkled: ' + str(correct_farkled[i])
    print 'farkled() returns: ' + str(farkled_result)
    if farkled_result == correct_farkled[i]: print 'PASS - farkled() RESULT IS CORRECT'
    else: 
        failedFarkled = failedFarkled + 1
        print '* * * * farkled() FAILED * * * *'
    i=i+1
    print '\n'
print 'farkled() failed ' + str(failedFarkled) + ' times.\n'



