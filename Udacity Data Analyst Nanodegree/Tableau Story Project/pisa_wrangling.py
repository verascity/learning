# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

pisa = pd.read_csv('pisa2012.csv', encoding='cp1252')
pisa_dict = pd.read_csv('pisadict2012.csv', encoding='cp1252')


new_pisa_names = ['']
for row in pisa_dict['x']:
    new_pisa_names.append(row)
    
pisa.columns = new_pisa_names

countries = {
    'Country code 3-character': {
        'China-Shanghai': 'China',
        'Chinese Taipei': 'Taiwan',
        'Connecticut (USA)': 'United States',
        'Florida (USA)': 'United States',
        'Hong Kong-China': 'China',
        'Korea': 'South Korea',
        'Macao-China': 'China',
        'Massachusetts (USA)': 'United States',
        'Perm(Russian Federation)': 'Russia',
        'Russian Federation': 'Russia',
        'United States of America': 'United States'
    }    
}

pisa = pisa.replace(countries)

final_cols = ['Country code 3-character', 'OECD country', 'International Grade', 
              'Gender', 'Attend <ISCED 0>', 'Mother<Highest Schooling>', 
              'Father<Highest Schooling>', 'Country of Birth International - Self',
              'International Language at Home', 
              'Age started learning <test language>',
              'Learning time (minutes per week)  - <test language>',
              'Index of economic, social and cultural status',
              'Math Anxiety - Worry That It Will Be Difficult',
              'Math Anxiety - Get Very Nervous', 
              'Math Anxiety - Feel Helpless', 
              'Math Anxiety - Worry About Getting Poor <Grades>',
              'Math Self-Concept - Not Good at Maths', 
              'Math Self-Concept- Get Good <Grades>',
              'Math Self-Concept - Learn Quickly', 
              'Math Self-Concept - Understand Difficult Work', 
              'Math Interest - Look Forward to Lessons', 
              'Math Interest - Enjoy Maths',
              'Instrumental Motivation - Worthwhile for Work',
              'Instrumental Motivation - Worthwhile for Career Chances', 
              'Instrumental Motivation - Important for Future Study', 
              'Instrumental Motivation - Helps to Get a Job',
              'Subjective Norms -Friends Do Well in Mathematics', 
              'Subjective Norms - Friends Enjoy Mathematics Tests', 
              'Subjective Norms - Parents Believe Studying Mathematics Is Important',
              'Subjective Norms - Parents Like Mathematics',
              'Math Self-Efficacy - Using a <Train Timetable>',
              'Math Self-Efficacy - Calculating TV Discount',
              'Math Self-Efficacy - Calculating Square Metres of Tiles',
              'Math Self-Efficacy - Understanding Graphs in Newspapers',
              'Plausible value 1 in mathematics',
              'Senate weight - sum of weight within the country is 1000']

pisa_final = pisa[final_cols]

clean_col_names = ['Country', 'OECD', 'International Grade', 'Gender',
                   'Attended Pre-Primary', 'Mother Highest Schooling',
                   'Father Highest Schooling', 'Birth Country', 'Home Language',
                   'Age Started Learning Test Language', 'Test Language Learning Time',
                   'ESCS Index', 'Math Anxiety - Worry That It Will Be Difficult',
              'Math Anxiety - Get Very Nervous', 
              'Math Anxiety - Feel Helpless', 
              'Math Anxiety - Worry About Getting Poor Grades',
              'Math Self-Concept - Not Good at Maths', 
              'Math Self-Concept- Get Good Grades',
              'Math Self-Concept - Learn Quickly', 
              'Math Self-Concept - Understand Difficult Work', 
              'Math Interest - Look Forward to Lessons', 
              'Math Interest - Enjoy Maths',
              'Instrumental Motivation - Worthwhile for Work',
              'Instrumental Motivation - Worthwhile for Career Chances', 
              'Instrumental Motivation - Important for Future Study', 
              'Instrumental Motivation - Helps to Get a Job',
              'Subjective Norms - Friends Do Well in Mathematics', 
              'Subjective Norms - Friends Enjoy Mathematics Tests', 
              'Subjective Norms - Parents Believe Studying Mathematics Is Important',
              'Subjective Norms - Parents Like Mathematics',
              'Math Self-Efficacy - Using a Train Timetable',
              'Math Self-Efficacy - Calculating TV Discount',
              'Math Self-Efficacy - Calculating Square Metres of Tiles',
              'Math Self-Efficacy - Understanding Graphs in Newspapers',
              'Score',
              'Weight']

pisa_final.columns = clean_col_names

print(pisa_final.columns)