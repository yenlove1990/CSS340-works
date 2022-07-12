#!/usr/bin/env python
# coding: utf-8

# In[24]:


class Fund:
    _fund_type = 0
    _fund_name =""
    _deposit = 0
    def __init__(self, deposit,type):
        self.set_type(type)
        self.set_deposit(deposit)
    def set_type(self,type):
        self._fund_type = type
        switcher = {
        0: "Money Market",
        1: "Prime Money Market",
        2: "Long Term Bond",
        3: "Short Term Bond",
        4: "500 Index Fund",
        5: "Capital Value Fund",
        6: "Growth Equity Fund",
        7: "Growth Index Fund",
        8: "Value Stock Index",
        9: "Value Fund",
        }
        self._fund_name = switcher.get(type, "invalid")
    def get_deposit(self):
        return self._deposit
    def get_type(self):
        return self._type
    def set_deposit(self,deposit):
        if deposit>=0:
            self._deposit = deposit
    def add_deposit(self, amount):
        if amount>0:
            self._deposit += amount
    def withdraw_deposit(self, amount):
        if amount<= self._deposit:
            self._deposit-= amount
    def __str__(self):
        return self._fund_name+" deposit : "+ str(self._deposit)
    def get_type(self):
        return self._fund_name
    

