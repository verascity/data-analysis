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

slope, intercept, r_1, p_1, std_err = linregress(early_grads['average_enrollment'],
                                                         early_grads['average_grads'])

plt.figure(1, figsize=(9, 6))
ax1 = sns.regplot(x='average_enrollment', y='average_grads', data=early_grads,
                  line_kws = {'label':'r={0:.2f}, p={1:.2f}'.format(r_1, p_1)})
ax1.legend()
plt.xlabel('Average Pre-K Enrollment', fontsize=16)
plt.ylabel('Average % of Total College Graduates', fontsize=16)
plt.suptitle('Pre-K Enrollment vs. Science Graduates \n (Per Country, 2009-2017)',
                                                         fontsize=18)
plt.savefig('early_ed_grads.png', format='png')

slope, intercept, r_2, p_2, std_err = linregress(early_pisa['average_enrollment'],
                                                         early_pisa['average_score'])

plt.figure(2, figsize=(9, 6))
ax2 = sns.regplot(x='average_enrollment', y='average_score', data=early_pisa, 
            line_kws = {'label':'r={0:.2f}, p={1:.2f}, r^2={2:.2f}'
                         .format(r_2,p_2,r_2**2)})
ax2.legend()
plt.xlabel('Average Pre-K Enrollment', fontsize=16)
plt.ylabel('Average PISA Score', fontsize=16)
plt.suptitle('Pre-K Enrollment vs. PISA Science Scores \n (Per Country, 2009-2017)',
             fontsize=18)
plt.savefig('early_ed_pisa.png', format='png')

early_ed_top = early_ed[early_ed['average_enrollment'] > 50.0]
early_pisa_top = pd.merge(early_ed_top, pisa, how='inner', on=['country', 'country_code'])

early_pisa_exp = pd.merge(early_pisa_top, exp[['country', 'average_expenditure']],
                      how='inner', on='country')

early_pisa_exp['exp_bins'] = pd.qcut(early_pisa_exp['average_expenditure'], 3, 
              precision=2, labels=['Low', 'Moderate', 'High'])

with sns.plotting_context(context='notebook', font_scale=1.3):
    g = sns.lmplot(x='average_enrollment', y='average_score', col='exp_bins', hue='exp_bins',
           data=early_pisa_exp, fit_reg=True)
    g = (g.set_titles("{col_name} Spending")
    .set_axis_labels('Average Enrollment', 'Average Score'))
    plt.suptitle('Enrollment vs. Scores, by Level of Government Spending',
             fontsize=18, x=0.5, y=1.1)
    plt.savefig('ed_grads_exp.png', format='png')
