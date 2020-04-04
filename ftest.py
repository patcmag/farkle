#!/usr/bin/python

import sys
import random
import return_score

x1 = [4,4,4]
x2 = [1,1,1]
x3 = [1,1,5]
x4 = [1,5]
x5 = [5,5]
x6 = [3,3,3,5]
x7 = [5,1,1,1]
x8 = [6,6,6,6]
x9 = [1,1,1,1]

rolls = [x1,x2,x3,x4,x5,x6,x7,x8,x9]
correct_scores = [400,750,250,150,100,350,800,1000,1000]

lam_tab = lambda x: '\t\t' if (x==2) else '\t'

i=0
for r in rolls:
    print str(r) + lam_tab(len(r)) + str(correct_scores[i])
    print 'return_score\t' + str(return_score.return_score(r))
    if return_score.return_score(r) == correct_scores[i]: print 'PASS'
    else: print 'FAIL'
    print '\n'
    i=i+1




