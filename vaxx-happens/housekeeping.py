# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 20:18:24 2019

@author: verascity

This is a little housekeeping script while I work out the kinks on this 
classifier; it will eventually go away!
"""

import pandas as pd

df1 = pd.read_csv('vaccine_df_01312019.csv')
df2 = pd.read_csv('vaccine_df_02242019.csv')
df1.columns = ['id', 'text', 'status']

vaccine_df = pd.concat([df1, df2])