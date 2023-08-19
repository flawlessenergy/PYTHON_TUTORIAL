#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
accounts_sid="YOUR ACCOUNT ID"
auth_token="YOUR_AUTH TOKEN"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
# NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "YOUR_STOCK_API_KEY"
#TODO Get your stock api key by creating an account on https://www.alphavantage.co
#to send SMS create an free account on Twilio

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#Get yesterday's closing stock price
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

diff_percent = round((difference / float(yesterday_closing_price)) * 100)
# print(diff_percent)
if difference > 0:
    body="The stock value as of yesterday is {} price increased by{} percent 🔻".format(STOCK_NAME,yesterday_closing_price,diff_percent)
else:
    body="The stock value of your {} stock as of yesterday is {} price declined by{} percent 🔻".format(STOCK_NAME,yesterday_closing_price,diff_percent)

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

client1=Client(accounts_sid,auth_token)
body=body



messege= client1.messages.create(
body=body,from_="+15736483550",
to="+917083096377")
print(messege.feedback)

#TODO send the same body messege using gmail(use smtplib in python) 


# In[ ]:




