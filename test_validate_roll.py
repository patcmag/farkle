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
x6 = [3,3,3,5] #350
x7 = [5,1,1,1] #800
x8 = [6,6,6,6] #1000
x9 = [1,1,1,1] #1000
x10 = [2,2,2,1,1] #400
x11 = [1,1,1,1,5] #1050
x12 = [6,6,6,6,6] #2000
x13 = [4,4,4,5,5] #500
x14 = [3,3,3,3,3,3] #3000
x15 = [1,1,1,4,4,4] #2500
x16 = [1,1,5,5,6,6] #1500
x17 = [1,2,3,4,5,6] #1500
x18 = [1] #100
x19 = [5] #50

#not valid rolls
x20 = ['a',4,44,5,5]
x21 = [3,'%',3,' ',4,1,1,1]
x22 = [2,3]
x23 = [1,0,4]
x24 = [1,1,2,2,4,5]
x25 = [0]

#valid
x26 = [5] #50
x27 = [5,5,5,1] #600
x28 = [1,5,1,5] #300

#not valid (farkles)
x29 = [2,2,3,4,5,6]
x30 = [4,2,6]
x31 = [6,6,2,3]
x32 = [3,4,6,2,2]
x33 = [3,3]
x34 = [4]

rolls = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,
            x20,x21,x22,x23,x24,x25,
                x26,x27,x28,
                    x29,x30,x31,x32,x33,x34]
correct_rolls = [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,
                    False,False,False,False,False,False,
                        True,True,True,
                            False,False,False,False,False,False]

#isolate an element, for debugging
# t = 28
# rolls = rolls[t-1:t]
# correct_rolls = correct_rolls[t-1:t]

#tests
i=0
failedIsValid = 0
for r in rolls:
    r_string = [str(x) for x in r]
    isValid_result = validate_roll.isValid(r_string)
    print str(r)
    print 'Actually valid: ' + str(correct_rolls[i])
    print 'isValid() returns: ' + str(isValid_result)
    if isValid_result == correct_rolls[i]: print 'PASS - isValid() RESULT IS CORRECT'
    else:
        failedIsValid = failedIsValid + 1 
        print '* * * * isValid() FAILED * * * *'
    i=i+1
    print '\n'
print 'isValid failed ' + str(failedIsValid) + ' times.\n'



