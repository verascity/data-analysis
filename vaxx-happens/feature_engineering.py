# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:51:41 2019

@author: verascity

This module will ultimately contain functions that will create new features
in a given dataframe, based on certain text characteristics in a column of 
that dataframe.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv('vaccine_df_01312019.csv')
df2 = pd.read_csv('vaccine_df_02242019.csv')
df1.columns = ['id', 'text', 'status']

vaccine_df = pd.concat([df1, df2])

vaccine_df['hashtags'] = vaccine_df.text.str.count('#')
vaccine_df['pings'] = vaccine_df.text.str.count('@')

#Eliminating outliers -- only one or two accounts are really throwing this off:
vaccine_df = vaccine_df[vaccine_df.hashtags <= 20]
vaccine_df = vaccine_df[vaccine_df.pings <= 20]


#plt.bar(vaccine_df.status, vaccine_df.hashtags)
#plt.bar(vaccine_df.status, vaccine_df.pings)

vaccine_df_limited = vaccine_df[(vaccine_df.status == 'Pro') | 
        (vaccine_df.status == 'Anti')]

ax = sns.boxplot(vaccine_df_limited.status, vaccine_df_limited.pings)