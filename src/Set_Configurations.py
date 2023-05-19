#import libraries

import requests


# Get Country from User

location = input("You wanna see top trends. But for which country?\n")


# Get Number of Top Trends from User

str = "We can bring upto 50 trends for " + location + ". How many do trends you want to see?\n"
trends = input(str)


# Get Time Interval in Minutes from User

str = "We are all good to bring the trends for you. \
      \nBut for which time interval do you want to track the tweets for these trends?\
      \nEnter the minutes:\n" 
minutes = input(str)



# Initiate Get Request from Trends API

url = 'https://9188-2a02-a210-2ec2-1480-58ec-cacd-5b36-a6cf.ngrok-free.app/trends_configurations/?no_of_top_trends=\
      ' + trends + '&country=' + location

x = requests.post(url)


# Initiate Get Request from Time API

url = 'https://9188-2a02-a210-2ec2-1480-58ec-cacd-5b36-a6cf.ngrok-free.app/timer/?minutes=\
      ' + minutes

x = requests.post(url)
