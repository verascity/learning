"""

This is the main project file for Udacity's Data Analyst Nanodegree
Project 3, "Investigate a Dataset." In this file I will read in and
analyze a CSV file containing information about no-shows to medical 
appointments in Brazil.

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('noshowappointments.csv')
print(df.head())