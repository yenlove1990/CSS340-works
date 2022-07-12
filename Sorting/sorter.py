#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import random
from sort import bubble_sort
from sort import insertion_sort
from sort import mergeSort
from sort import iterativeMergeSort
from sort import quickSort
from sort import shellSort

sort = str(sys.argv[1])
size = int(sys.argv[2])
ifPrint = str(sys.argv[3])
list = [random.randint(-9999, 9999) for x in range(size)]
copy_list = list[i for i in list]
if sort == "bubble":
    bubble_sort(list)
if sort == "insertion":
    insertion_sort(list)
if sort == "merge":
    mergeSort(list)
if sort == "imerge":
    iterativeMergeSort(list)
if sort == "quick":
    quickSort(list)
if sort == "shell":
    shellSort(list)
if ifPrint == "PRINT":
    print("unsorted list:"copy_list)
    print(list)
    

