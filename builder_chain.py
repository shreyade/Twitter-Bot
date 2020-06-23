#!/usr/bin/env python
# coding: utf-8

# In[1]:


import suffix_builder
import prefix_builder
from dictionary import Dictionary
from functools import *


# In[2]:


NONWORD = "/n"


# In[3]:


#reads the file
def readingLines(fileName):
    with open(fileName, encoding='utf-8') as file:
        yield file.read()


# In[4]:


#generates prefix-suffix pairs based on the words passed in
def pairs_generation(fileName, lineGenerator):
    generator = lineGenerator(fileName)
    
    #initial prefix:
    currPrefix = prefix_builder.make_new_prefix(NONWORD, NONWORD) #represents a tuple of nonwords
    for line in generator:
        words = line.split()
        for word in words:
            #updating the prefix:
            currPrefix = prefix_builder.shift(currPrefix, word)
            yield (currPrefix, word)
    yield (currPrefix, '\n')


# In[5]:


#adding prefix-suffix pair to the markov chain
def chain_add(chain, pair):
    chainKey = chain.get(pair[0])
    newChainVal = suffix_builder.add(chainKey, pair[1])
    return chain.put(pair[0], newChainVal)


# In[6]:


def building_chain(add_prefix, generator, dictionary):
    return reduce(lambda x, y: chain_add(x, y), generator, dictionary)


# In[7]:


def build(filename):
    return building_chain(None, pairs_generation(filename, readingLines), Dictionary())


# In[ ]:





# In[ ]:




