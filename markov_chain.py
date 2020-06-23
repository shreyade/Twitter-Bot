#!/usr/bin/env python
# coding: utf-8

# In[1]:


import builder_chain
import generate_chain
import random
from TwitterAPI import TwitterAPI
from functools import *
import time
import json


# In[2]:


consumer_key='tZ6jzxDu3DYsm68jComTX0mGq'
consumer_secret='1Qxx1HdsTzq97CDYYDJ7DyP9e0STK4S4wjEoYav5GFmTQek2O1'
access_token_key='901824647091458048-BlmJp1CPFlqWLjGXZZX7AjA4xGwEXq4'
access_token_secret='ON36ISFFdRkn2ShEQVeyIsqTRj2Ow3QJICq6P2pPFCv0D'


# In[3]:


api = TwitterAPI(consumer_key,consumer_secret,access_token_key,access_token_secret)


# In[4]:


#fetches 200 Tweets with the TwitterAPI 
List = []
t = api.request('statuses/user_timeline', {'screen_name': "realDonaldTrump", 'count': 200})
List += [t.json()]


# In[5]:


randomInt = random.randint(1, (len(List) - 4))
randomSelection = List[randomInt:randomInt+3]


# In[ ]:


#write randomly selected 3 words and the rest of the tweets picked up
with open("Output.txt", "w", encoding='utf-8') as text_file:
    for item in randomSelection:
        text_file.write(item + " ")
    for item in reducedList:
        text_file.write(item + " ")


# In[ ]:


def randomFunc(bound):
    return random.randint(1, bound)


# In[ ]:


file_name = 'Output.txt'
chain = builder_chain.build(file_name)
number = 20

#use generator class to generate tweet
output_string = generate_chain.generateChain(chain, randomFunc, number, '\n')

#posts it to twitter account
api.request("statuses/update", {'status': "*TWITTER BOT THAT SPEAKS LIKE DONALD TRUMP*: " + outstr})

#print the output of the tweet generation
print(output_string)


# In[ ]:





# In[ ]:




