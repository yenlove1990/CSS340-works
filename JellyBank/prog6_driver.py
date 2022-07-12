#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import BinarySearchTree.py
import Account.py
import Fund.py
import Transaction.py
from queue import *


if __name__ == '__main__':
    account_list = BinarySearchTree()
    queue = Queue(maxsize=0)
    ID_list= []
    with open("BankTransIn.txt") as file:
        for line in file:
            line = line.strip()
            queue.put(line)
    while not queue.empty():
        line = queue.get()
        line = line.split()
        action = line[0]
        if(action =="O"):
            last_name = line[1]
            first_name = line[2]
            accountID = line[3]
            if account_list.get(accountID) == None:
                account_list.put(accountID,Account(last_name,first_name,accountID))
                ID_list.append(accountID)
            else:
                print("ERROR: Account "+accountID+" is already open. Transaction refused.")
        elif(action =="D"):
            accountID = line[1]
            amount = int(line[2])       
            account = accountID[0:len(accountID)-1]
            fund = accountID[-1]
            if account_list.get(account) != None:
                account_list.get(account).fund_list[int(accountID[-1])].add_deposit(amount)
                account_list.get(account).add_transaction(Transaction(accountID,action,amount))
            else:
                print("ERROR: Account "+account+ "not found. Transferal refused.")

        elif(action =="T"):
            accountID = line[1]
            account = accountID[0:4]
            amount = int(line[2])
            accountID_2 = line[3]
            account2 = accountID_2[0:4]
            if account_list.get(account)==None:
                print("ERROR: Account "+str(accountID)+" not found. Transferal refused.")
            elif account_list.get(account2)==None:
                print("ERROR: Account "+str(account2)+" not found. Transferal refused.")
            elif account_list.get(account).sum()>= amount:
                if account_list.get(account).fund_list[int(accountID[-1])].get_deposit()>=amount:
                    account_list.get(account).fund_list[int(accountID[-1])].withdraw_deposit(amount)
                    account_list.get(account2).fund_list[int(accountID_2[-1])].add_deposit(amount)
                    account_list.get(account).add_transaction(Transaction(accountID,action,amount,accountID_2))
            else: 
                print("insufficient")
        elif(action =="H"):
            accountID = line[1]
            if(account_list.get(accountID[0:4])==None):
                print("ERROR: Account "+str(accountID)+" not found.")
            elif(len(accountID)==5):
                account_list.get(accountID[0:4]).display(accountID[-1])
            elif(len(accountID)==4):
                print("Transaction History for "+account_list.get(accountID).get_name()+" by fund")
                account_list.get(accountID).display()
        elif(action =="W"):
            accountID = str(line[1])
            amount = int(line[2])
            if account_list.get(account).fund_list[int(accountID[-1])].get_deposit()>= amount:
                num =account_list.get(account).fund_list[int(accountID[-1])].get_deposit()
                account_list.get(account).fund_list[int(accountID[-1])].set_deposit(num-amount)
                account_list.get(account).add_transaction(Transaction(accountID,action,amount))
            elif accountID[-1] =="0" or accountID[-1]== "1":
                if account_list.get(account).cover(amount):
                    if accountID[-1] =="0":
                        amount-=account_list.get(account).fund_list[int(accountID[-1])].get_deposit()
                        account_list.get(account).fund_list[int(accountID[-1])].set_deposit(0)
                        account_list.get(account).fund_list[int(accountID[-1])].set_deposit(account_list.get(account).fund_list[int(accountID[1])]-amount)
                        account_list.get(account).add_transaction(Transaction(accountID,action,amount))
                    else:
                        amount-=account_list.get(account).fund_list[int(accountID[-1])].get_deposit()
                        account_list.get(account).fund_list[int(accountID[-1])].set_deposit(0)
                        account_list.get(account).fund_list[int(accountID[-1])].set_deposit(account_list.get(account).fund_list[int(accountID[0])]-amount)
                        account_list.get(account).add_transaction(Transaction(accountID,action,amount))
                else:
                    print("ERROR: Not enough funds to withdraw "+line[2]+" from "+account_list.get(account).get_name()+" "
    + account_list.get(account).fund_list[int(accountID[-1])].get_type())
                    account_list.get(account).add_transaction(Transaction(accountID,action,amount,"",True))

            else: 
                print("ERROR: Not enough funds to withdraw "+line[2]+" from "+account_list.get(account).get_name()+" "
    + account_list.get(account).fund_list[int(accountID[-1])].get_type())
                account_list.get(account).add_transaction(Transaction(accountID,action,amount,"",True))

    print("Processing Done. Final Balances")
    for i in ID_list:
        print(account_list.get(i).get_name()," Account ID: ",str(account_list.get(i).get_accountID()))
        for num in range(10):
            print("   "+str(account_list.get(i).fund_list[num]))


# In[ ]:




