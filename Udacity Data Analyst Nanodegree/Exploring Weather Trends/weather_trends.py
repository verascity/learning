# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 13:48:04 2018

This script analyzes weather_data.csv to look for trends in yearly average
temperature, both globally and locally to New York City, from 1750 to 2013. 
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


weather = pd.read_csv("weather_data.csv")

#print(weather.describe()) #Describe reveals one missing value in ny_temp.
#print(weather[weather['ny_temp'].isna()]) #Reveals missing year is 1780
weather = weather.bfill() #The ny_temp for 1779 is an outlier at 0.25, so backfilling makes the most sense.

weather["ny_mov_avg"] = weather["ny_temp"].rolling(window=10).mean()
weather["global_mov_avg"] = weather["global_temp"].rolling(window=10).mean()
