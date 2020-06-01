from tkinter import Tk, Button, Label, BOTTOM, TOP, LEFT, Canvas

dotSize = 8 #toggle dice size

def oneDot(lv):
    halfX = (lv[2]-lv[0])/2
    halfY = (lv[3]-lv[1])/2
    x1 = lv[0] + halfX - dotSize
    y1 = lv[1] + halfY - dotSize
    x2 = lv[2] - halfX + dotSize
    y2 = lv[3] - halfY + dotSize
    
    return [x1,y1,x2,y2]


def twoDot(lv):
    quarterX = (lv[2]-lv[0])/4
    quarterY = (lv[3]-lv[1])/4
    #dot 1
    d1x1 = lv[0] + quarterX - dotSize
    d1y1 = lv[1] + quarterY - dotSize
    d1x2 = lv[0] + quarterX + dotSize
    d1y2 = lv[1] + quarterY + dotSize
    #dot 4
    d4x1 = lv[2] - quarterX - dotSize
    d4y1 = lv[3] - quarterY - dotSize
    d4x2 = lv[2] - quarterX + dotSize
    d4y2 = lv[3] - quarterY + dotSize

    return [[d1x1,d1y1,d1x2,d1y2], [d4x1,d4y1,d4x2,d4y2]]

def threeDot(lv):
    td = twoDot(lv)
    return [td[0],td[1],oneDot(lv)]

def fourDot(lv):
    quarterX = (lv[2]-lv[0])/4
    quarterY = (lv[3]-lv[1])/4

    #dot 2
    d2x1 = lv[2] - quarterX - dotSize
    d2y1 = lv[1] + quarterY - dotSize
    d2x2 = lv[2] - quarterX + dotSize
    d2y2 = lv[1] + quarterY + dotSize

    #dot 3
    d3x1 = lv[0] + quarterX - dotSize
    d3y1 = lv[3] - quarterY - dotSize
    d3x2 = lv[0] + quarterX + dotSize
    d3y2 = lv[3] - quarterY + dotSize

    #dots 1 and 4
    twoDots = twoDot(lv)
    return [twoDots[0], [d2x1,d2y1,d2x2,d2y2], [d3x1,d3y1,d3x2,d3y2], twoDots[1]]

def fiveDot(lv):
    fd = fourDot(lv)
    return [fd[0],fd[1],fd[2],fd[3],oneDot(lv)]

def sixDot(lv):
    halfY = (lv[3]-lv[1])/2
    quarterX = (lv[2]-lv[0])/4

    d5x1 = lv[0] + quarterX - dotSize
    d5y1 = lv[1] + halfY - dotSize
    d5x2 = lv[0] + quarterX + dotSize
    d5y2 = lv[1] + halfY + dotSize

    d6x1 = lv[2] - quarterX - dotSize
    d6y1 = lv[3] - halfY - dotSize
    d6x2 = lv[2] - quarterX + dotSize
    d6y2 = lv[3] - halfY + dotSize

    fd = fourDot(lv)
    return [fd[0],fd[1],fd[2],fd[3],[d5x1,d5y1,d5x2,d5y2], [d6x1,d6y1,d6x2,d6y2]]


def getDieDotCoords(die, lv):
    if die==1: return oneDot(lv)
    if die==2: return twoDot(lv)
    if die==3: return threeDot(lv)
    if die==4: return fourDot(lv)
    if die==5: return fiveDot(lv)
    if die==6: return sixDot(lv)
