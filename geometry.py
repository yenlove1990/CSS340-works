#!/usr/bin/env python
# coding: utf-8

# In[17]:


import math 
#
# Module containing geometric shapes
#
class Circle:
    def __init__(self, x = 0, y = 0,radius = 0):
        if x >= 0:
            self._x = x
        else:
            self._x = 0
        if y >= 0:
            self._y = y
        else:
            self._y = 0
        if radius >= 0 :
            self._radius = radius
        else:
            self._radius = 0
            
    def set_x(self, x):
        if x >= 0:
            self._x = x
        else:
            self._x = 0
            
    def set_y(self, y):
        if y >= 0:
            self._y = y
        else:
            self._y = 0
            
    def set_radius(self, radius):
        if radius >= 0 :
            self._radius = radius
        else:
            self._radius = 0
            
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_radius(self):
        return self._radius
    
    def area(self):
        return math.pow(self._radius,2)*math.pi
    
    def perimeter(self):
        return self._radius*2*math.pi
    
    def contains_point(self, x, y):
        distance = math.dist([x, y],[self._x, self._y])
        if distance > self._radius:
            return False
        else:
            return True


# In[20]:



print("Partial Testing for CSS340 Lab1")
c1 = Circle(3, 3, 7)
c2 = Circle()
print("First Circle Perimeter: " + str(c1.perimeter()))
print("First Circle Area: " + str(c1.area()))
 
c2.set_x(3)
c2.set_y(3)
c2.set_radius(2)
if c2.contains_point(4, 3.7):
    print("(4, 3.7) is within circle two")
else:
    print("(4, 3.7) is not within circle two")
print("Moving second Circle")
c2.set_x(3 + c2.get_x())
if c2.contains_point(4, 3.7):
    print("(4, 3.7) is within circle two")
else:
    print("(4, 3.7) is not within circle two")


# In[ ]:





# In[ ]:




