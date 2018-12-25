# -*- coding: utf-8 -*-

import pandas as pd

pisa = pd.read_csv('pisa2012.csv', encoding='cp1252')
pisa_dict = pd.read_csv('pisadict2012.csv', encoding='cp1252')


new_pisa_names = ['']
for row in pisa_dict['x']:
    new_pisa_names.append(row)
    
pisa.columns = new_pisa_names

print(pisa.head())