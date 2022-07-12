#!/usr/bin/env python
# coding: utf-8

# In[72]:



def bubble_sort(list):
     for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

def insertion_sort(list):
    for place in range(1,len(list)):
        temp = list[place]
        i = place
        while i > 0 and list[i - 1] > temp:
            list[i] = list[i-1]
            i -= 1
        list[i] = temp
def merge_sort_worker(list, first, last):
    if first < last:
        mid = (first + last) // 2
        merge_sort_worker(list, first, mid)
        merge_sort_worker(list, mid + 1, last)
        merging(list, first, mid, last)
def mergeSort(list):
    merge_sort_worker(list, 0, len(list)-1)
def iterativeMergeSort(list):
    width = 1
    num = len(list)
    while (width < num):
     
        bot=0;
        while (bot < num):
            last = min(bot+(width*2-1), num-1)
            mid = min(bot+width-1,num-1)
            merging(list, bot, mid, last)
            bot += width*2

        width *= 2
    return list



def merging(list, first, mid, last):
    size = last - first + 1
    temp_list =[0] * size
    first1 = first 
    last1 = mid
    first2 = mid+1
    last2 = last
    index = 0
    while first1 <= last1 and first2 <= last2:
        if list[first1] < list[first2]:
            temp_list[index] = list[first1]
            first1 +=1
        else: 
            temp_list[index] = list[first2]
            first2+=1
        index += 1
    while first1 <= last1:
        temp_list[index] = list[first1]
        first1 +=1
        index +=1
    while first2 <= last2 :
        temp_list[index] = list[first2]
        first2 +=1
        index +=1
    for index in range(size):
        list[first] = temp_list[index]
        first+=1




def partition(list, low, high):
    pivot = list[high]
    i = low - 1
    for j in range(low, high):
        if list[j]<= pivot:
            i =i +1
            list[i], list[j]= list[j], list[i]
    list[i+1],list[high] = list[high], list[i+1]
    return i+1
def quick_sort_worker(list,low, high):
    if low < high:
        pi = partition(list, low, high)
        quick_sort_worker(list, low, pi - 1)
        quick_sort_worker(list, pi+1, high)
def quickSort(list):
    quick_sort_worker(list,0,len(list)-1)   
def shellSort(list):
    size = len(list)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            temp = list[i]
            j = i
            while j >= gap and temp < list[j - gap]:
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        if gap == 2:
            gap = 1
        else:
            gap = int(gap / 2.2)

