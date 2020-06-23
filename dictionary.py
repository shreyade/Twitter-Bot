#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Dictionary:

    def __init__(self):
        self.dictionary = {}
        
    def put(self, k, v):
        newDictionary = Dictionary()
        newDictionary.dictionary = {**self.dictionary, **{k:v}}
        return newDictionary

    def get(self, key):
        if key in self.dictionary:
            return self.dictionary[key]
        return None

    def keys(self):
        return list(self.dictionary.keys())

    def values(self):
        return list(self.dictionary.values())


# In[ ]:




