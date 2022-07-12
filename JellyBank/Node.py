#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self, key, value = None):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None
    def is_leaf(self):
        return self.left_child == None and self.right_child == None
    def __str__(self):
        return str(self.key) + " " + str(self.value)

