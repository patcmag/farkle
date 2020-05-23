#!/usr/bin/python

import gui
import subprocess as sp
import tkinter as tk
# import farkle as fk
from tkinter import *


class Die():
    def __init__(self,can,dieID,numDots,x1,y1,x2,y2):
        self.can=can #canvas on current playArea frame
        self.dieID = dieID #ID of this specific die (not value)
        self.id=self.can.create_rectangle((x1,y1,x2,y2),fill="white") #this die's outline
        self.dots=[] #references to this die's dots
        self.selected_status=False #whether this has been clicked/in 'selected' state
        dotCoords = gui.getDieDotCoords(numDots,[x1,y1,x2,y2]) #get dot coords based on die location
        
        #add ovals to the [dots] class attribute  
        if numDots==1: self.dots.append(self.can.create_oval(dotCoords,fill="black"))
        else:
            for dot in dotCoords: self.dots.append(self.can.create_oval(dot,fill="black"))
                
        #bind the die rectangle and the dots to the same event
        #(button press changes color and 'selected' state)        
        self.can.tag_bind(self.id,"<ButtonPress-1>",self.set_color)    
        for dot_ref in self.dots: self.can.tag_bind(dot_ref,"<ButtonPress-1>",self.set_color)
        self.color_change=True
        # print 'die ' + dieID + ' has been created in GUI'

    def get_selected_status(self):
        return self.selected_status

    def get_dieID(self):
        return self.dieID

    def set_color(self,event=None):
        self.color_change = not self.color_change
        color='white'
        if not self.color_change: color = "red"
        self.can.itemconfigure(self.id,fill=color)
        self.selected_status = not self.selected_status #toggle between False and True

