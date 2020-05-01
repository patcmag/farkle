#!/usr/bin/python
import sys
import random
import gui
import subprocess as sp
from tkinter import Tk, Button, Label, BOTTOM, TOP, LEFT, Canvas
from subprocess import Popen
import os

root = Tk()

welcomeLabel = Label(root,
                    font = ('Helvetica',16,'bold italic'),
                    foreground = 'black',
                    background = 'white',
                    padx=25,pady=10,
                    text='welcome to farkle v2')
welcomeLabel.pack(side=TOP)

canvas1 = Canvas(root,height=500,width=550)
canvas1.create_rectangle(3,3,550,500) 
canvas1.pack(side=TOP)

def startGame():
    Popen(["python", "farkle.py"])

clickToPlay = Button(root,
                text='startGame',
                command=startGame,      #close GUI for now
                padx=25,pady=50)

clickToPlay.pack()
root.mainloop()  #https://stackoverflow.com/questions/8683217/when-do-i-need-to-call-mainloop-in-a-tkinter-application

