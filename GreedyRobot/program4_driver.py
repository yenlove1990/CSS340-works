#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import Point.py
import Greedy_Robot.py
#takes 4 nums form the terminal
x0 = int(sys.argv[1])
y0 = int(sys.argv[2])
xt = int(sys.argv[3])
yt = int(sys.argv[4])
#declare the start point
start_point = Point(x0,y0)
#declare the end point
end_point = Point(xt,yt)
#input the two point into the greedy robot constructor
robot = Greedy_Robot(start_point, end_point)
#call the path finder
robot.path_finder()

