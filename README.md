<img src="https://github.com/tarvihafatima/Twitter-Trends-Analysis/assets/26660037/51cb913c-bcfb-4af6-b76f-409a21b8fe10" width="100" height="50">

# Twitter-Trends-Analysis

Twitter is a popular social media platform where users post messages, or tweets, on various topics. The goal of this project is to compare the message volume of the top trending subjects on Twitter over a specific period.

## Installing / Getting started

You will need: 

* Python 3.11 or above
* pip3
* uvicorn
* ngrok
* pubnub
* cassandra
* Astra

#### Python Libraries

```shell
pip install request
pip install pubnub>=7.1.0
pip install fastapi
pip install cassandra
pip install pandas
pip install selenium
pip install beautifulsoup4
pip install webdriver-manager
```

## Development Setup

#### 1-Clone Directory

```shell
git clone https://github.com/tarvihafatima/Twitter-Trends-Analysis
```

#### 2-Install Dependencies and Python Libraries

#### 3-Create Account on PubNub and Download SDK

Account Register: https://admin.pubnub.com/#/register

```shell
pip install 'pubnub>=7.1.0'
```

#### 4-Create Account on Astra DB and Generate token and Bundle

Account Register: https://www.datastax.com/lp/astra-registration?redirect_uri=https://astra.datastax.com/welcome&

#### 5-Create Database and Keyspace(Schema) on Cassandra

Create Database and Keyspace: https://astra.datastax.com/org/58fc3d82-d8f3-4124-b2f8-f32115f82bfe?createDatabase=1

#### 6-Update Configuration File

* Open the Configuration file (/src/data/configuration.yaml)
* Update PubNub and Cassandra credentials received from the previous steps
* Download the bundle file from Astra DB and place in /src/data/ directory

#### 7-Run the Project 



## Features

While our project will compare the popularity and engagement levels of top 3 trending topics by analyzing the number of tweets containing the trending subjects in Netherlands at every 1,5 and 10th minute, our goal is to let users:

* #### Analyse the popularity of Trending topics in Netherlands or Anywhere in the world.
* #### Compare the tweet volume containing the trending subjects at any given time interval. 

## Links

* Github Repository: https://github.com/tarvihafatima/Twitter-Trends-Analysis 
* Python Download: https://www.python.org/downloads/
* PubNub Account Register: https://admin.pubnub.com/#/register
* Astra Account Register: https://www.datastax.com/lp/astra-registration?redirect_uri=https://astra.datastax.com/welcome&
* Create Database and Keyspace in Astra: https://astra.datastax.com/org/58fc3d82-d8f3-4124-b2f8-f32115f82bfe?createDatabase=1

