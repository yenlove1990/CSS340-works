#!/usr/bin/env python
# coding: utf-8

# In[21]:


class Transaction:
    _accountID=''
    _action=''
    _num=0
    _accountID2= 0
    fail = False
    def __init__(self,accountID, action, num,accountID2 = "", fail = False):
        self._accountID = accountID
        self._action = action
        self._num = num
        self._accountID2 = accountID2 
        self.fail = fail
    def __str__(self):
        if self.fail:
            if self._action =="D":
                return self._action+" "+self._accountID+" "+str(self._num)+ "(Failed)"
            if self._action =="W":
                return self._action+" "+self._accountID+" "+str(self._num)+"(Failed)"
            if self._action =="T":
                return self._action+" "+self._accountID+" "+str(self._num)+" "+self._accountID2+"(Failed)"
        else:
            if self._action =="D":
                return self._action+" "+self._accountID+" "+str(self._num)
            if self._action =="W":
                return self._action+" "+self._accountID+" "+str(self._num)
            if self._action =="T":
                return self._action+" "+self._accountID+" "+str(self._num)+" "+self._accountID2
    def get_account(self):
        return self._accountID

