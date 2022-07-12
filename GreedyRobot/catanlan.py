#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
#the method counts the catanlan number
def catanlan(n):
    if n< 0 :
        return False
    if n == 0 or n == 1:
        return 1
    temp = 0 
    for i in range(n):
        temp= temp + catanlan(i)*catanlan(n-i-1)
    
    return temp

input = int(sys.argv[1])
catalan(input)

