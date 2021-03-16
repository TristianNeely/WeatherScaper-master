import pandas as pd
from firebase import firebase
import requests
from bs4 import BeautifulSoup
from firebase import firebase
import json
import sys


page = requests.get('https://forecast.weather.gov/MapClick.php?lat=44.64196&lon=-124.04110#.YDUib-hKiUk')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id="seven-day-forecast-body")
#print(week)

items = week.find_all(class_='tombstone-container')
#print(items[0])

print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

period_name = [item.find(class_='period-name').get_text() for item in items]
short_description = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]


weather_stuff = (
    {
        'period': period_name,
        'short_description': short_description,
        'temperatures': temperatures,
    })


print(weather_stuff)

#weather_stuff.to_csv('webscrapper.csv')

weather = pd.read_csv (r'C:\Users\neely_tristian\Desktop\webScaper-master\webscrapper.csv')

# Create JSON File
weather.to_json (r'C:\Users\neely_tristian\Desktop\JSON Webscrapper\JSONwebscrapper.json')





firebase = firebase.FirebaseApplication("https://weather-scraper-b6ce2-default-rtdb.firebaseio.com/", None)

result = firebase.post('/weather-scraper-b6ce2-default-rtdb/Weather', weather_stuff)
