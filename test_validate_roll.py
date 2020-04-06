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
# x13 = [4,4,4,5,5] #500
# x14 = [3,3,3,3,3,3] #3000
# x15 = [1,1,1,4,4,4] #2500
# x16 = [1,1,5,5,6,6] #1500
# x17 = [1,2,3,4,5,6] #1500
# x18 = [1] #100
# x19 = [5] #50

#not valid rolls
x13 = ['a',4,44,5,5] #500
x14 = [3,'%',3,' ',4,1,1,1] #3000
x15 = [2,3] #2500
x16 = [1,0,4] #1500
x17 = [1,1,2,2,4,5] #1500
x18 = [0] #100

#valid
x19 = [5] #50

rolls = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19]
# correct_scores = [400,750,250,150,100,350,800,1000,1000,400,1050,2000,500,3000,2500,1500,1500,100,50]

#for pretty output
# def formatTab(x):
#     if x in [1,2]: return '\t\t\t'
#     elif x in [3,4,5]: return '\t\t'
#     else: return '\t'

#tests
i=0
for r in rolls:
    r_string = [str(x) for x in r]
    if validate_roll.isValid(r_string) == True: print 'PASS - IS VALID'
    else: print '* * * * FAIL * * * *'
    print '\n'
    i=i+1




