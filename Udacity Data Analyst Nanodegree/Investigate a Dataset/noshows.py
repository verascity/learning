"""
This is my code submission for Udacity's Data Analyst Nanodegree Project 
3, "Investigate a Dataset." 

"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.display.max_columns = None

#Functions:
def between_params(df, col, params):
    """
    Takes in a dataframe, column name, and tuple or list of 2
    parameters, and returns the dataframe with the column's values now
    falling between the parameters.
    """
    df = df[(df[col] >= params[0]) & (df[col] <= params[1])]
    return df
    
def obj_to_date(col):
    """
    Takes in a column with a datetime-like string object and returns the 
    column as a date object.
    """
    col = pd.to_datetime(col, infer_datetime_format=True).dt.date
    return col

def bar_plots_from_x(df, lim_list, label_list, title=None):
    """
    Takes in a dataframe, list of limits, list of labels, and optional title,
    and outputs a figure and bar charts with the same X-axis, corresponding to
    the dataframe index, and Y-axes showing the column data. Setting y-limits
    helps keep the chart proportionate and avoids overestimating differences.
    """
    
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
    fig.suptitle(title)
    plt.show()
    
def stacked_hist(seriesone, seriestwo, labelone, labeltwo, title=None):
    """
    Takes in two Series, two labels, and an optional title, and returns a 
    stacked histogram with the appropriate labels and title. 
    """
    plt.hist(seriesone, bins=20, color='black', alpha=0.5, label=labelone)
    plt.hist(seriestwo, bins=20, color='blue', alpha=0.5, label=labeltwo)
    plt.title(title)
    sns.despine(top=True)
    plt.legend()
    plt.show()
 
def normal_table(df):
    """
    Takes a dataframe containing two columns and returns that same dataframe, 
    reshaped into a normalized pivot table.
    """
    cols = list(df.columns)
    df = df.groupby(cols).size()
    df = df.unstack(level=1)
    df = df.div(df.sum(axis=1), axis=0)
    return df

if __name__ == "__main__":
    #Read in file:
    df = pd.read_csv('noshowappointments.csv')
    
    #Data cleaning/wrangling:
    df = df.rename(index=str, columns={"Hipertension":"Hypertension", 
                                   "Handcap" : "Disability"})
    df['AppointmentDay'] = obj_to_date(df['AppointmentDay'])
    df['ScheduledDay'] = obj_to_date(df['ScheduledDay'])
    df['TimeBetween'] = (df['AppointmentDay'] - df['ScheduledDay']).dt.days
    df = between_params(df, 'Age', (0, 95))
    df = between_params(df, 'TimeBetween', (0, 100))
    df = df.drop(['AppointmentID', 'AppointmentDay', 'ScheduledDay', 'PatientId', 'Neighbourhood'], axis=1)

    #Question 1: What features are most associated with no-shows?
    noshows = df.groupby('No-show').mean()
    print(noshows) #There aren't a lot of strong associations!
    noshows = noshows[['Age', 'TimeBetween', 'SMS_received']]
    bar_plots_from_x(noshows, [50,30,1], ['Age in Years', 'Time Btw. Schd./Appt.', 'Prob. of SMS Recvd.'], 
                 title='No-Shows by Age, Time Waiting, and SMS Received')

    #Question 2: How are ages distributed between shows and no-shows? 
    #View disrtributions as histogram:
    no_show_ages = df[df['No-show'] == 'Yes']['Age']
    yes_show_ages = df[df['No-show'] == 'No']['Age']
    stacked_hist(no_show_ages, yes_show_ages, 'No-show', 'Show', title='Distribution of Show/No-Show Ages')
           
    #Create and view age group data:
    bin_edges = [0, 18, 37, 55, 95]
    bins = ['child', 'young adult', 'adult', 'senior']
    df['age_group'] = pd.cut(df['Age'], bin_edges, labels=bins, include_lowest=True)
    df_ages = df[['age_group', 'No-show']]
    df_ages = normal_table(df_ages)
    print(df_ages)
    df_ages.plot(kind='bar', ylim=(0,1), title='Proportions of Show/No-Show By Age Group')
    sns.despine(top=True)