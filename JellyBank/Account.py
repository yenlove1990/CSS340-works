#!/usr/bin/env python
# coding: utf-8

# In[72]:


get_ipython().run_line_magic('run', 'Fund.ipynb')
class Account:
    fund_list= []
    transaction_list = []
    _first_name = ""
    _last_name = ""
    _accountID = ""
    _count=0
    def __init__(self,last_name,first_name, accountID):
        self._first_name = first_name
        self._last_name = last_name
        self._accountID = accountID
        self.fund_list= []
        self.transaction_list = []
        for i in range(10):
            self.fund_list.append(Fund(0,i))
    def get_accountID(self):
        return self._accountID
    def sum(self):
        sum = 0
        for account in self.fund_list:
            sum+= account.get_deposit()
        return sum
    def add_transaction(self,transaction):
        self.transaction_list.append(transaction)
        self._count+=1
    def __str__(self):
        return self._accountID+" "+"deposit - "+str(self.sum())
    def add_account(self,account):
        fond_list[self._count] = fond
    def display(self,id = -1):
        tl = self.transaction_list
        if id == -1:
            for i in range(10):
                print(self.fund_list[i].get_type()+ " : $"+str(self.fund_list[i].get_deposit()))
                for t in tl:
                    temp = str(self._accountID)+str(id)
                    if t.get_account() == self._accountID+str(i):
                        print(str(t))
        else:
            print("Transaction History for "+self.get_name()+" "+self.fund_list[int(id)].get_type()+": "+str(self.fund_list[int(id)].get_deposit()))
            for i in tl:
                temp = str(self._accountID)+id
                if i.get_account() == temp:
                    print(str(i))
    def get_name(self):
        return self._first_name+" "+self._last_name
    def cover(self,num):
        return self.fund_list[0].get_deposit()+self.fund_list[1].get_deposit()>= num

