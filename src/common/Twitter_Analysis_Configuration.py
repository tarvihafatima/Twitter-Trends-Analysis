#import libraries
from fastapi import FastAPI, Query

# initialize global variables
g_no_of_top_trends = 3
g_country = 'netherlands'
g_minutes = 10

app = FastAPI()
 
# Set Twitter Trends Configurations    
@app.post("/trends_configurations/")
def add_config(no_of_top_trends: int = Query(default= 3), country: str = Query(default= 'netherlands')):
    global g_no_of_top_trends, g_country
    g_no_of_top_trends = no_of_top_trends
    g_country = country.lower()
    return g_no_of_top_trends, g_country

# Get Twitter Trends Configurations   
@app.get("/trend_read_configurations/")
def read_config():
    global g_no_of_top_trends, g_country
    return g_no_of_top_trends, g_country

# Set Timer 
@app.post("/timer/")
def add_config(minutes: int = Query(default= 10)):
    global g_minutes
    g_minutes = minutes
    return g_minutes

# Get Twitter Trends Configurations   
@app.get("/get_timer/")
def read_config():
    global g_minutes
    return g_minutes
