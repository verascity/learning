# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 13:48:04 2018

This script analyzes weather_data.csv to look for trends in yearly average
temperature, both globally and locally to New York City, from 1950 to 2013. 
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv("weather_data.csv")
print(weather.describe())