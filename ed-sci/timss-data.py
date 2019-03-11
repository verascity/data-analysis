"""
This script will compare reported worldwide enrollment in early childhood education,  
from 2005-2016 (per UNICEF), with 8th grade science scores on the TIMSS 2015, to provide evidence
towards an answer to the question: Does early childhood education boost science achievement?
"""

import pandas as pd

early_ed = pd.read_csv('net_enrollment.csv', na_values='..', 
                       header=None).dropna(thresh=11)
exp = pd.read_csv('expenditures.csv', na_values='..',
                  header=None).dropna(thresh=11)
timss = pd.read_csv('timss2015.csv')

#Some cleaning:
col_names = ['country', 'country_code', '2005', '2006', '2007', '2008', 
               '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', 
               'avg_over_time']
early_ed.columns = col_names
exp.columns = col_names
timss.columns = timss.columns.str.replace('Education System',
                                          'country')
timss = timss.rename(str.lower, axis='columns')

early_ed_and_timss = pd.merge(early_ed, timss, how='inner', on='country')
exp_and_timss = pd.merge(exp, timss, how='inner', on='country')