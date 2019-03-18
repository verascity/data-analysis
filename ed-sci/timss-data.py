"""
This script will compare reported worldwide enrollment and government expenditure
in early childhood education from 2009-2017 with with science scores 
on the Programme for International Assessment 2009, 2012, and 2015, as well as
tertiary enrollment in science programs 2009-2017 (all via the World Bank database), 
to provide evidence towards answering the question: Does early childhood 
education boost science achievement on a global basis?
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress 

sns.set_style('darkgrid')

early_ed = pd.read_csv('net_enrollment.csv', na_values='..').dropna(thresh=8)
exp = pd.read_csv('expenditures.csv', na_values='..').dropna(thresh=8)
pisa = pd.read_csv('pisa_mean.csv', na_values='..').dropna(thresh=3)
stem_grads = pd.read_csv('stem_grads.csv', na_values='..').dropna(thresh=8)
nsms_grads = pd.read_csv('nsms_grads.csv', na_values='..').dropna(thresh=8)

sci_grads = stem_grads.copy()
sci_grads.iloc[:, 2:8].add(nsms_grads.iloc[:, 2:8])

#Creating averages:
early_ed['average_enrollment'] = early_ed.mean(axis=1, skipna=True, numeric_only=True)
exp['average_expenditure'] = exp.mean(axis=1, skipna=True, numeric_only=True)
pisa['average_score'] = pisa.mean(axis=1, skipna=True, numeric_only=True)
sci_grads['average_grads'] = sci_grads.mean(axis=1, skipna=True, numeric_only=True)

#Merging:
early_pisa = pd.merge(early_ed, pisa, how='inner', on=['country', 'country_code'])
exp_pisa = pd.merge(exp, pisa, how='inner', on=['country', 'country_code'])
early_grads = pd.merge(early_ed, sci_grads, how='inner', on=['country', 'country_code'])
exp_grads = pd.merge(exp, sci_grads, how='inner', on=['country', 'country_code'])

#Possible correlation here:
#plt.scatter(early_pisa['average_enrollment'], early_pisa['average_score'])

#Another possible correlation?:
#plt.scatter(early_grads['average_enrollment'], early_grads['average_grads'])

#No clear correlation here:
#plt.scatter(exp_pisa['average_expenditure'], exp_pisa['average_score'])

#Or here:
#plt.scatter(exp_grads['average_expenditure'], exp_grads['average_grads'])

'''Based on the above, expenditure doesn't seem to correlate much, but early
childhood enrollment might.'''

ep_corr = early_pisa['average_enrollment'].corr(early_pisa['average_score'])
eg_corr = early_grads['average_enrollment'].corr(early_grads['average_grads'])
#print(ep_corr, eg_corr) #Looks like I was wrong about that early_grads correlation.

slope, intercept, r_value, p_value, std_err = linregress(early_pisa['average_enrollment'],
                                                         early_pisa['average_score'])

print(r_value, p_value, r_value**2)

#ax = sns.regplot(x='average_enrollment', y='average_score', data=early_pisa, 
#            line_kws = {'label':'r={0:.2f}, p={1:.2f}, r^2={2:.2f}'
#                         .format(r_value,p_value,r_value**2)})
#ax.legend()
#plt.xlabel('Average Net Enrollment in Pre-Primary Programs')
#plt.ylabel('Average PISA Science Score')
#plt.suptitle('Pre-Primary Enrollment vs. PISA Scores \n')
#plt.title('(Per Country, 2009-2017)')

early_pisa_exp = pd.merge(early_pisa, exp[['country', 'average_expenditure']],
                      how='inner', on='country')

early_pisa_exp['exp_bins'] = pd.qcut(early_pisa_exp['average_expenditure'], 3, 
              precision=2, labels=['Low', 'Medium', 'High'])

g = sns.lmplot(x='average_enrollment', y='average_score', col='exp_bins', hue='exp_bins',
           data=early_pisa_exp)
g = (g.set_titles("{col_name} Expenditure")
    .set_axis_labels('Average Enrollment', 'Average Score')
    .fig.subplots_adjust(wspace=0.01))