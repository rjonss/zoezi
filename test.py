#!/usr/bin/python3
import datetime

today = datetime.datetime.now()
today_formatted = today.strftime("%Y-%m-%d")
print(today_formatted)

future_date = today + datetime.timedelta(days=5)
print(future_date.strftime("%Y-%m-%d"))