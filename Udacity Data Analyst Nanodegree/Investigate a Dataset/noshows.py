"""
This is the main project file for Udacity's Data Analyst Nanodegree Project 
3, "Investigate a Dataset." In this file I will read in and analyze a CSV file 
containing information about no-shows to medical appointments in Brazil.

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.display.max_columns = None

def load_data(filename):
    df = pd.read_csv(filename)
    return df


df = load_data('noshowappointments.csv')

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
avoid extreme outliers.
"""
def between_params(df, col, params):
    df = df[(df[col] >= params[0]) & (df[col] <= params[1])]
    return df
    
def obj_to_date(col):
    col = pd.to_datetime(col, infer_datetime_format=True).dt.date
    return col
 
df = df.set_index('AppointmentID')
df = df.rename(index=str, columns={"Hipertension":"Hypertension", 
                                   "Handcap" : "Disability"})

df['AppointmentDay'] = obj_to_date(df['AppointmentDay'])
df['ScheduledDay'] = obj_to_date(df['ScheduledDay'])
df['TimeBetween'] = (df['AppointmentDay'] - df['ScheduledDay']).dt.days

df = between_params(df, 'Age', (0, 95))
df = between_params(df, 'TimeBetween', (0, 100))
df = df.drop(['AppointmentDay', 'ScheduledDay', 'PatientId', 'Neighbourhood'], axis=1)


"""
Question 1: I chose this project thinking that handicap or welfare status might 
have an impact, but after using groupby().mean() to look through the features
associated with no-shows, there actually doesn't seem to be much there.

The features that appear most closely associated with no-shows are age and
timebetween, with a slight possibility of association with SMS_received.
"""

noshows = df.groupby('No-show').mean()
#print(noshows) # There aren't a lot of strong associations!
#print(df.describe())

noshows = noshows[['Age', 'TimeBetween', 'SMS_received']]

def bar_plots_from_x(df, lim_list, label_list):
    '''
    This function takes in a dataframe, list of limits, and list of labels,
    and outputs a figure and bar charts with the same X-axis, corresponding to
    the dataframe index, and Y-axes showing the column data. Setting y-limits
    helps keep the chart proportionate and avoids overestimating differences.
    '''
    
    cols = list(df.columns)
    ax_no = len(cols)
    axes = tuple('ax'+str(i) for i in range(1,ax_no+1))
    fig, axes = plt.subplots(len(axes), 1, figsize=(8, 10))
    x_val = df.index
    colors = "bgrcmykw"
        
    for i, ax in enumerate(axes):
        ax.bar(x_val, df[cols[i]], color=colors[i])
        ax.set_ylim([0,lim_list[i]])
        ax.set_xlabel(df.index.name)
        ax.set_ylabel(label_list[i])
        ax.tick_params(axis='both', length=0)
                       
    sns.despine(top=True)
    plt.show()
    
    
#bar_plots_from_x(noshows, [50,30,1], ['Age in Years', 'Time Btw. Schd./Appt.', 'Prob. of SMS Recvd.'])

"""
Question 2: If no-shows seem slightly more likely to be young, how young are
they? In other words, what age group most represents no-shows?
"""

bin_edges = [0, 18, 37, 55, 95]
bins = ['child', 'young adult', 'adult', 'senior']
df['age_group'] = pd.cut(df['Age'], bin_edges, labels=bins)
print(df.head())