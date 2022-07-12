#!/usr/bin/env python
# coding: utf-8

# In[45]:


import Node.py
class BinarySearchTree:
    _count=0
    def __init__(self):
        self._count = 0
        self._root = None
    def size(self):
        return self._count
    def is_empty(self):
        return self._count == 0
    def get(self, key):
        current_node = self._root
        while current_node != None:
            if current_node.key == key:
                return current_node.value
            elif current_node.key > key:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return None
    def __getitem__(self, key):
        return self.get(key)
    def put(self, key, value):
        if self.is_empty():
            self._root = Node(key, value)
            self._count = 1
            return
        current_node = self._root
        while True:
            if current_node.key == key:
                current_node.value = value
                return
            elif current_node.key > key:
                if current_node.left_child == None:
                    new_node = Node(key, value)
                    current_node.left_child = new_node
                    break
                else:
                    current_node = current_node.left_child
            else:
                if current_node.right_child == None:
                    new_node = Node(key, value)
                    current_node.right_child = new_node
                    break
                else:
                    current_node = current_node.right_child
        self._count = self._count + 1
    def remove(self,key):
        if self.is_empty():  
            return root
        if self._root.key >key:
            self._root.right_child =remove(self._root.right_child,key)
        elif self._root.key <key:
            self._root.left_child =remove(self._root.left_child,key)
        else:
            if root.right_child ==None:
                return root.left_child
            if root.left_child ==None:
                return root.right_child
            temp = root.right_child
            temp_key = temp.key
            while temp.left_child != None :
                temp = temp.left_child
                temp_key = temp.key
            root.right_child = remove(root.right_child,root.key)
        return root
    def __setitem__(self, key, data):
        self.put(key, data)
    def __str__(self):
        return "s"


# In[ ]:




