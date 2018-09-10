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
"""
#Plot the data:
plt.figure(figsize=(10, 5)) 
plt.plot(weather["year"], weather["ny_mov_avg"], 'orange', weather["year"], weather["global_mov_avg"], 'blue')
plt.xlabel("Year")
plt.ylabel("Temperature in Celsius")
plt.suptitle("10-Year Moving Average Temperatures, Globally and in New York City, 1750-2015") #I prefer suptitle for spacing.
plt.legend(["New York", "Global"])

#Calculate the correlation coefficient for the two moving averages:
corr = weather["ny_mov_avg"].corr(weather["global_mov_avg"]) 
print(corr)
"""

"""
After looking at this data, I was curious about how other cities would
compare, so I generated a new csv with a random sample of five cities.
"""

weather2 = pd.read_csv("weather_data2.csv")
weather2["location"] = weather2["city"] + ", " + weather2["country"]
weather2 = weather2[["year", "location", "city_temp", "global_temp"]]
weather2 = weather2.interpolate()


grouped = weather2[["year", "city_temp"]].groupby(weather2["location"])
print(grouped.get_group("Canberra, Australia"))
