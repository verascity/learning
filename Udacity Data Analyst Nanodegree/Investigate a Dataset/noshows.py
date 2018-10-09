"""

This is the main project file for Udacity's Data Analyst Nanodegree Project 
3, "Investigate a Dataset." In this file I will read in and analyze a CSV file 
containing information about no-shows to medical appointments in Brazil.

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('noshowappointments.csv')

"""
For the sake of decluttering, I'm going to reset the index to the
AppointmentID, which is unique to every row and can serve as the primary
key. There are no rows with missing data, so this shouldn't pose a problem.

I'm also going to drop and add some columns. I know that neighbourhood does
not interest me, so I'm going to drop that. I am interested in repeat no-shows,
so I'm going to create a new column to indicate duplicates, then drop the
very unwieldy 'PatientId' column.
"""

df = df.set_index('AppointmentID')
df['Duplicate'] = df['PatientId'].duplicated()
df = df.drop(['PatientId', 'Neighbourhood'], axis=1)