# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 13:48:04 2018

This script analyzes weather_data.csv to look for trends in yearly average
temperature, both globally and locally to New York City, from 1750 to 2013. 
"""

import pandas as pd
import matplotlib.pyplot as plt


weather = pd.read_csv("weather_data.csv")

#print(weather.describe()) #Describe reveals one missing value in ny_temp.
#print(weather[weather['ny_temp'].isna()]) #Reveals missing year is 1780
weather = weather.bfill() #The ny_temp for 1779 is an outlier at 0.25, so backfilling makes the most sense.

#Calculate 10-year moving averages:
weather["ny_mov_avg"] = weather["ny_temp"].rolling(window=10).mean() 
weather["global_mov_avg"] = weather["global_temp"].rolling(window=10).mean()

#Plot the data:
plt.figure(figsize=(10, 5)) 
plt.plot(weather["year"], weather["ny_mov_avg"], 'orange', weather["year"], weather["global_mov_avg"], 'blue')
plt.xlabel("Year")
plt.ylabel("Temperature in Celsius")
plt.suptitle("10-Year Moving Average Temperatures, Globally and in New York City, 1750-2015") #I prefer suptitle for spacing.
plt.legend(["New York", "Global"])

"""
After looking at this data, I'm curious about how other cities will
compare, so I go back and generate a new csv with a random sample of five cities.

Originally, when I ran this data, I used all the years in the global data and 
started from 1750 again. However, that turned out to not be very useful. First,
three of my cities only have data starting around 1825-1875. Also, it actually
became harder to see the trends once more data was included. So I'm going to 
retool this part to only include the 20th and 21st centuries.
"""

weather2 = pd.read_csv("weather_data2.csv")
weather2["location"] = weather2["city"] + ", " + weather2["country"]
weather2 = weather2[["year", "location", "city_temp", "global_temp"]]
weather2 = weather2.interpolate()

#Applies 10-year moving average to each city:
weather2["city_mov_avg"] = weather2.groupby(weather2["location"]).city_temp.apply(lambda x: x.rolling(10).mean())
weather2["global_mov_avg"] = weather["global_mov_avg"]
weather2 = weather2[weather2["year"] >= 1900]
grouped = weather2.groupby(weather2["location"])

#Giving each city its own dataframe:
denver = grouped.get_group("Denver, United States")
pretoria = grouped.get_group("Pretoria, South Africa")
ufa = grouped.get_group("Ufa, Russia")
vientiane = grouped.get_group("Vientiane, Laos")
wuhan = grouped.get_group("Wuhan, China")

plt.figure(figsize=(12,8))
plt.plot(weather2["year"], weather2["global_mov_avg"], "blue", 
         denver["year"], denver["city_mov_avg"], "green", 
         pretoria["year"], pretoria["city_mov_avg"], "black", 
         ufa["year"], ufa["city_mov_avg"], "tan",
         vientiane["year"], vientiane["city_mov_avg"], "red",
         wuhan["year"], wuhan["city_mov_avg"], "pink")
plt.xlabel("Year")
plt.ylabel("Temperature in Celsius")
plt.suptitle("10-Year Moving Average Temperatures, Globally and in Five Cities, 1900-2015")
plt.legend(["Global", "Denver, USA", "Pretoria, SA", "Ufa, Russia", "Vientiane, Laos", "Wuhan, China"])