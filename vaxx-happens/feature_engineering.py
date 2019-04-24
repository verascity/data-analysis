# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:51:41 2019

@author: verascity

This module will ultimately contain functions that will create new features
in a given dataframe, based on certain text characteristics in a column of 
that dataframe.
"""

import pandas as pd

df1 = pd.read_csv('vaccine_df_01312019.csv')
df2 = pd.read_csv('vaccine_df_02242019.csv')
df1.columns = ['id', 'text', 'status']

vaccine_df = pd.concat([df1, df2])

vaccine_df['hashtags'] = vaccine_df.text.str.count('#')
vaccine_df['pings'] = vaccine_df.text.str.count('@')

