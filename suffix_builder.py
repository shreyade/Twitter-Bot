#!/usr/bin/env python
# coding: utf-8

# In[1]:


from dictionary import Dictionary
from functools import *


# In[2]:


def add(suffix, word):
    #if suffix is nothing
    if suffix is None:
        return Dictionary().put(word, 1) 
    elif suffix.get(word) != None:
        return suffix.put(word, 1 + suffix.get(word)) #update the value in the dictionary
    else:
        return suffix.put(word, 1) #put it in the dictionary with val one


# In[3]:


def choose(chain, prefix, randomFunc):
    suffix = chain.get(prefix)
    totalCount = 0
    for key in suffix.dictionary:
        totalCount = totalCount + 1 #increment the totalCount 
    
    #find a random number in between 1 and the totalCount
    randomNum = randomFunc(totalCount)
    
    #generate a probability list
    probabilityList = [y for lst in [makeList(key, suffix.get(key)) for key in suffix.dictionary] for y in lst]
    #return one of the values of the probability test
    return probabilityList[randomNum-1]


# In[4]:


#recursive function
def makeList(key, count):
    if count == 0: #base case
        return []
    if count > 0: #recursive case
        return [key] + makeList(key, count - 1)


# In[ ]:




