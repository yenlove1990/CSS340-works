#!/usr/bin/env python
# coding: utf-8

# In[13]:


class Point:
    x_coordinate = 0
    y_coordinate = 0
    #constuctor
    def __init__(self, x , y):
        if type(x)==int:
            self.x_coordinate = x
        if type(y)==int:
            self.y_coordinate = y
    #getter for X
    def getX(self):
        return self.x_coordinate
    #getter for Y
    def getY(self):
        return self.y_coordinate
    #overriding tostring
    def __str__(self):
        return "("+str(self.getX())+","+str(self.getY())+")"

