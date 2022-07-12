#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math

"""
The TimeSpan program takes 3 input as its variable, it has the ability to cancel the decimals and
simplify even if input is greater than 60 or less than -60. 
The +-*/ operator is overrided in the program
"""
class TimeSpan:
    
    #define constructor to take in time inputs.
    def __init__(self, second = 0, minute = 0, hour = 0):
        self.set_time(second, minute, hour)
        self.decimal()
        self.simplify()
        
    #the overriding to string function to output hours, minutes, and seconds
    def __str__(self):
        text= "Hours: {hour}, Minutes: {minute}, Seconds: {second}"
        return text.format(hour = int(self.get_hours()),minute = int(self.get_minutes()),
                           second = int((self.get_seconds())))  
    
    #define the setter for variable hour
    def set_hours(self, hour):
        self._hour = float(hour)
        
    #define the setter for variable minute
    def set_minutes(self, minute):
        self._minute  = float(minute)
        
    #define the setter for variable second
    def set_seconds(self, second):
        self._second  = float(second)
        
    #define the getter for variable hour
    def get_hours(self):
        return self._hour
    
    #define the getter for variable minute
    def get_minutes(self):
        return self._minute
    
    #define the getter for variable second
    def get_seconds(self):
        return self._second

    #define a method to cancel the decimals in the variables
    def decimal(self):
        if self.get_hours()% 1 != 0:
            self.set_minutes(int(self.get_minutes()+self.get_hours()%1*60))
        if self.get_minutes()%1 != 0 :
            self.set_seconds(int(self.get_seconds()+self.get_minutes()%1*60))
        self.set_seconds(round(self.get_seconds(),0))
    
    #setter for all three variables
    def set_time(self, second, minute, hour):
        self.set_seconds(second)
        self.set_minutes(minute)
        self.set_hours(hour)
    
    #define the method to simplify the variables and limit its boundary
    def simplify(self):
        if self.get_seconds() >= 60 or self.get_seconds() <= -60:
            self.set_minutes(self.get_minutes()+int(self.get_seconds()/60))
            self.set_seconds(self.get_seconds()%60)
        if self.get_minutes() >= 60 or self.get_minutes() <= -60:
            self.set_hours(self.get_hours()+int(self.get_minutes()/60))
            self.set_minutes(self.get_minutes()%60)
        if self.get_seconds() < 0:
            self.set_minutes(self.get_minutes()-1)
            self.set_seconds(self.get_seconds()+60)
        if self.get_minutes() < 0:
            self.set_hours(self.get_hours()-1)
            self.set_minutes(self.get_minutes()+60)
        if self.get_hours() < 0 and self.get_minutes() > 0:
            self.set_minutes(self.get_minutes()+int(self.get_seconds()-60))
            self.set_hours(self.get_hours()+1)
        self.set_seconds(int(self.get_seconds()))
        self.set_minutes(int(self.get_minutes()))
        self.set_hours(int(self.get_hours()))
        
    #define the overriding method for + operator within TimeSpan
    def __add__(self, other):
        second = self.get_seconds()+other.get_seconds()
        minute = self.get_minutes()+other.get_minutes()
        hour = self.get_hours()+other.get_hours()
        return TimeSpan(second, minute, hour)
    
    #define the overriding method for - operator within TimeSpan
    def __sub__(self, other):
        second = self.get_seconds()-other.get_seconds()
        minute = self.get_minutes()-other.get_minutes()
        hour = self.get_hours()-other.get_hours()
        return TimeSpan(second, minute, hour)
    
    #define the overriding method for -self operator within TimeSpan
    def __neg__(self):
        to_return = TimeSpan()
        second = 0 - self.get_seconds()
        minute = 0 - self.get_minutes()
        hour = 0 - self.get_hours()
        if hour > 0:
            to_return = TimeSpan(second, minute, hour)
        else:
            to_return.set_time(second,minute,hour)
        return to_return
    
    #define the overriding method for < operator within TimeSpan
    def __lt__(self, other):
        if self.get_hours()<other.get_hours():
            return True
        elif self.get_minutes()<other.get_minutes():
            return True
        elif self.get_seconds()<other.get_seconds():
            return True
        return False
    
    #define the overriding method for == operator within TimeSpan
    def __eq__(self, other):
        if self.get_hours() == other.get_hours():
            if self.get_minutes() == other.get_minutes():
                if self.get_seconds() == other.get_seconds():
                    return True
        return False
    
    #define the overriding method for <= operator within TimeSpan
    def __le__(self, other):
        if self.get_hours()<=other.get_hours():
            if self.get_minutes()<=other.get_minutes():
                if self.get_seconds()<=other.get_seconds():
                    return True        
        return False
    
    #define the overriding method for != operator within TimeSpan
    def __ne__(self, other):
        return not self==other
    
    #define the overriding method for > operator within TimeSpan
    def __gt__(self, other):
        if self.get_hours()>other.get_hours():
            return True
        elif self.get_minutes()>other.get_minutes():
            return True
        elif self.get_seconds()>other.get_seconds():
            return True
        return False
    
    #define the overriding method for >= operator within TimeSpan
    def __ge__(self, other):

        return self==other or self>other

    #define the overriding method for * operator within TimeSpan
    def __mul__(self, other):
        second = self.get_seconds()*other.get_seconds()
        minute = self.get_minutes()*other.get_minutes()
        hour = self.get_hours()*other.get_hours()
        return TimeSpan(second, minute, hour)
    
    #define the overriding method for / operator within TimeSpan
    def __truediv__(self, other):
        second = self.get_seconds()/other.get_seconds()
        minute = self.get_minutes()/other.get_minutes()
        hour = self.get_hours()/other.get_hours()
        return TimeSpan(second, minute, hour)
    
    #define the overriding method for *= operator within TimeSpan
    def __imul__(self, other):
        second = self.get_seconds()*other.get_seconds()
        minute = self.get_minutes()*other.get_minutes()
        hour = self.get_hours()*other.get_hours()
        return TimeSpan(second, minute, hour)
    
    #define the overriding method for /= operator within TimeSpan
    def __idiv__(self, other):
        second = self.get_seconds()/other.get_seconds()
        minute = self.get_minutes()/other.get_minutes()
        hour = self.get_hours()/other.get_hours()
        return TimeSpan(second, minute, hour)
    
    #define the overriding method for -= operator within TimeSpan
    def __isub__(self, other):
        if self<other:
            second = self.get_seconds()-other.get_seconds()
            minute = self.get_minutes()-other.get_minutes()
            hour = self.get_hours()-other.get_hours()
            to_return = TimeSpan()
            to_return.set_seconds(second)
            to_return.set_minutes(minute)
            to_return.set_hours(hour)
            return to_return
        second = self.get_seconds()-other.get_seconds()
        minute = self.get_minutes()-other.get_minutes()
        hour = self.get_hours()-other.get_hours()
        return TimeSpan(second, minute, hour)
    
    #define the overriding method for += operator within TimeSpan
    def __iadd__(self, other):
        second = self.get_seconds()+other.get_seconds()
        minute = self.get_minutes()+other.get_minutes()
        hour = self.get_hours()+other.get_hours()
        return TimeSpan(second, minute, hour)

