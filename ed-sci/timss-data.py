"""
This script will compare reported worldwide enrollment and government expenditure
in early childhood education from 2009-2017 with with science scores 
on the Programme for International Assessment 2009, 2012, and 2015, as well as
tertiary enrollment in science programs 2009-2017 (all via the World Bank database), 
to provide evidence towards answering the question: Does early childhood 
education boost science achievement on a global basis?
"""

import pandas as pd

early_ed = pd.read_csv('net_enrollment.csv', na_values='..').dropna(thresh=8)
exp = pd.read_csv('expenditures.csv', na_values='..').dropna(thresh=8)
pisa = pd.read_csv('pisa_mean.csv', na_values='..').dropna(thresh=3)
stem_grads = pd.read_csv('stem_grads.csv', na_values='..').dropna(thresh=8)
nsms_grads = pd.read_csv('nsms_grads.csv', na_values='..').dropna(thresh=8)

sci_grads = stem_grads.copy()
sci_grads.iloc[:, 2:8].add(nsms_grads.iloc[:, 2:8])

#Creating averages:


#Evaluating overlap:
#early_ed_and_pisa = pd.merge(early_ed, pisa, how='inner', on=['country', 'country_code'])
#exp_and_pisa = pd.merge(exp, pisa, how='inner', on=['country', 'country_code'])
#early_ed_and_grads = pd.merge(early_ed, sci_grads, how='inner', on=['country', 'country_code'])
#exp_and_grads = pd.merge(exp, sci_grads, how='inner', on=['country', 'country_code'])