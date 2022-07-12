#!/usr/bin/env python
# coding: utf-8

# In[34]:


import Point.py
import sys
class Greedy_Robot:
    #initialize two variables 
    start_point = Point(0,0)
    end_point = Point(0,0)
    
    #takes two point for constructor
    def __init__(self,start_point,end_point):
        self.start_point = start_point
        self.end_point = end_point
    
    #it handle the input if it is at the same space
    def path_finder(self):
        if self.start_point.getX() == self.end_point.getX() and self.start_point.getY() == self.end_point.getY():
            print("Treasure is under your feet, greedy robot")
        else:
            self.walk_master(self.start_point,self.end_point)
    #this seperate the points and put it into walk
    def walk_master(self, point1, point2):
        self.walk(point1.getX(),point1.getY(),point2.getX(),point2.getY(),"")
    #starts walking to destination
    def walk(self,sx,sy,ex,ey, move):
            xmove= move
            ymove= move
            if(sx==ex and sy==ey):
                print(move)
            if sy!=ey:
                if ey>sy:
                    xmove= xmove + "N"
                    self.walk(sx,sy+1,ex,ey,xmove)
                else:
                    xmove= xmove + "S"                        
                    self.walk(sx,sy-1,ex,ey,xmove)
            if sx!=ex :  
                if ex>sx:
                    ymove= ymove + "E"
                    self.walk(sx+1,sy,ex,ey,ymove)
                else:
                    ymove= ymove + "W"
                    self.walk(sx-1,sy,ex,ey,ymove)

