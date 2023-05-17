#import libraries
from typing import Optional
from fastapi import FastAPI, Query


# initialize global variables
no_of_top_trends = 3
country = 'netherlands'

app = FastAPI()
 
# Set Twitter Trends Configurations    
@app.post("/trends_configurations/")
def add_config(no_of_top_trends: int = Query(default= 3), country: str = Query(default= 'netherlands')):
    no_of_top_trends = no_of_top_trends
    country = country
    return no_of_top_trends, country

# Get Twitter Trends Configurations   
@app.get("/trend_read_configurations/")
def read_config():
    return no_of_top_trends, country

