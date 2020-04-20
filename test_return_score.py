#!/usr/bin/python

import sys
import random
import return_score

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
x20 = [1,5,1,5] #300
x21 = [5,5,5] #500
x22 = [5,5,5,1] #600
x23 = [1,1,2,2,5,2] #450

rolls = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23]
correct_scores = [400,750,250,150,100,350,800,1000,1000,400,1050,2000,500,3000,2500,1500,1500,100,50,300,500,600,450]

#isolate an element, for debugging
# t = 23
# rolls = rolls[t-1:t]
# correct_scores = correct_scores[t-1:t]

#for pretty output
def formatTab(x):
    if x in [1,2]: return '\t\t\t'
    elif x in [3,4,5]: return '\t\t'
    else: return '\t'

#tests
i=0
failedReturnScore = 0
for r in rolls:
    print str(r) + formatTab(len(r)) + str(correct_scores[i])
    print 'return_score\t\t' + str(return_score.return_score(r))
    if return_score.return_score(r) == correct_scores[i]: print 'PASS'
    else: 
        failedReturnScore = failedReturnScore + 1
        print '* * * * FAIL * * * *'
    print '\n'
    i=i+1
print 'return_score() failed ' + str(failedReturnScore) + ' times.\n'




