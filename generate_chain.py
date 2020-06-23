#!/usr/bin/env python
# coding: utf-8

# In[1]:


import prefix_builder
import suffix_builder
import random
from functools import *


# In[2]:


def wordList(chain, pre, randomFunc, word_count, NONWORD):
        #recursively call method choose_word
        
        #suffix.choose_word generates a random word from the suffix probability list
        return (suffix_builder.choose(chain, pre, randomFunc)) + wordList(chain, prefix_builder.shift(pre,NONWORD), randomFunc, word_count - 1, '\n')


# In[3]:


def generateChain(chain, randomFunc, word_count, NONWORD):
    
    #create the word_list 
    word_list = wordList(chain, ('\n',  '\n'), randomFunc, word_count, NONWORD)
    
    #start generating the final list 
    #capitalize the first word
    stringBuilder = word_list[0].capitalize() + " "
    for i in range(1, len(word_list)):
        stringBuilder += word_list[i] + " "
    return stringBuilder 


# In[ ]:




