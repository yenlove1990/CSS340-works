#!/usr/bin/env python
# coding: utf-8

# In[16]:



import random
import timeit
import matplotlib.pyplot as plt
import random

#iterating search BigO of n
def find1(list, val):  
    for i in range(len(list)):
        if list[i]==val:
            return i 

#sort the deepcopy of input list then binary search BigO of nlogn
def find2(list, val): 
    newList = []
    for item in list:
        newList.append(item)
    newList.sort()
    return find4(newList,val)

#use build-in in to search if the val is in the list of, BigO of n
def find3(list, val):
    if val in list:
        return True 

# binary search BigO of logn
def find4(list, val):
    top=len(list)-1
    bot= 0
    mid= 0
    while(bot <= top):
        mid= (top+bot)//2           
        if list[mid]>val:
            top =mid-1
        elif list[mid]<val:
            bot = mid+1
        else:
            return mid 
    return False


#Driver code for testing
#creating an list size = 100
for i in range(1000):
    list= []
    for x in range(i+1):
        list.append(x)  
    list.append(99999)
#creating list to hold the execution time
timeForfind1 = []
timeForfind2 = []
timeForfind3 = []
timeForfind4 = []
#count how many times it has been exected
count = []

#executing the four method
for i in range(1000):
    t = timeit.Timer("find1(list,99999)", "from __main__ import find1, list")
    duration = t.timeit(i)
    timeForfind1.append(duration)
    
    t = timeit.Timer("find2(list,99999)", "from __main__ import find2, list")
    duration = t.timeit(i)
    timeForfind2.append(duration)
    
    t = timeit.Timer("find3(list,99999)", "from  __main__ import find3, list")
    duration = t.timeit(i)
    timeForfind3.append(duration)

    t = timeit.Timer("find4(list,99999)", "from  __main__ import find4, list")
    duration = t.timeit(i)
    timeForfind4.append(duration)
    count.append(i)


font1 = {'family':'serif','color':'blue','size':20}   
plt.title("Running Time vs. Execution times", fontdict = font1)
plt.xlabel("Execution times")
plt.ylabel("Running time")
plt.plot(count, timeForfind1, label="find1")
plt.plot(count, timeForfind2, label="find2")
plt.plot(count, timeForfind3, label="find3")
plt.plot(count, timeForfind4, label="find4")
plt.legend()
plt.show()

