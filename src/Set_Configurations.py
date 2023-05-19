#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import libraries

import requests

location = input("You wanna see top trends. But for which country?\n")
str = "We can bring upto 50 trends for " + location + ". How many do trends you want to see?\n"
trends = input(str)

str = "We are all good to bring the trends for you. \
      \nBut for which time interval do you want to track the tweets for these trends?\
      \nEnter the minutes:\n" 
minutes = input(str)

url = 'https://9188-2a02-a210-2ec2-1480-58ec-cacd-5b36-a6cf.ngrok-free.app/trends_configurations/?no_of_top_trends=\
      ' + trends + '&country=' + location

x = requests.post(url)

url = 'https://9188-2a02-a210-2ec2-1480-58ec-cacd-5b36-a6cf.ngrok-free.app/timer/?minutes=\
      ' + minutes

x = requests.post(url)


# In[ ]:




