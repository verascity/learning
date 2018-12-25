# -*- coding: utf-8 -*-

import pandas as pd

#pisa = pd.read_csv('pisa2012.csv', encoding='cp1252')
#pisa_dict = pd.read_csv('pisadict2012.csv', encoding='cp1252')


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

