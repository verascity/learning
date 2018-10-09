"""
This is the main project file for Udacity's Data Analyst Nanodegree Project 
3, "Investigate a Dataset." In this file I will read in and analyze a CSV file 
containing information about no-shows to medical appointments in Brazil.

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns = None

df = pd.read_csv('noshowappointments.csv')

"""
Data Cleaning/Wrangling:
    
For the sake of decluttering, I'm going to reset the index to the
AppointmentID, which is unique to every row and can serve as the primary
key. There are no rows with missing data, so this shouldn't pose a problem.

I'm also going to edit the columns. I know that neighbourhood does
not interest me, so I'm going to drop that. I am interested in repeat no-shows,
so I'm going to create a new column to indicate duplicates, then drop the 
unwieldy 'PatientId' column. Finally, I'm going to fix some mispelled 
column names.

Also, the 'ScheduledDay'/'AppointmentDay' columns are mostly interesting because
of what they imply about the distance between them, so I'm going to make a 
column for time differences.

Finally, after looking through the data, I realized there are some wonky values 
in the 'Age' and new 'TimeBetween' columns, so I'll also restrict those to 
avoid outliers.
"""

df = df.set_index('AppointmentID')
df['Duplicate'] = df['PatientId'].duplicated()
df = df.drop(['PatientId', 'Neighbourhood'], axis=1)
df = df.rename(index=str, columns={"Hipertension":"Hypertension", 
                                   "Handcap" : "Disability"})
df = df[(df['Age'] >= 0) & (df['Age'] <= 95)]

df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'], infer_datetime_format=True).dt.date
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'], infer_datetime_format=True).dt.date
df['TimeBetween'] = df['AppointmentDay'] - df['ScheduledDay']
df = df.drop(['AppointmentDay', 'ScheduledDay'], axis=1)
df = df[df['TimeBetween'] >= '0 days 00:00:00']


"""
Question 1: I chose this project thinking that handicap or welfare status might 
have an impact, but after using groupby() and describe() to look through the features
associated with no-shows, there actually isn't much there.
"""

noshows = df.groupby('No-show').mean()
#print(noshows) # There aren't a lot of strong associations!
#print(df.describe())




"""
Question 2: What features are associated with repeat no-shows?
"""

#repeats = df[df['No-show'] == 'Yes'].groupby('Duplicate')