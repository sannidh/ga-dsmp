# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# code starts here
df = pd.read_csv(path)
p_a = len(df[df['fico'] > 700]) / len(df)
p_b = len(df[df['purpose'] == 'debt_consolidation'])/ len(df)
df1 = df[df['purpose'] == 'debt_consolidation']
p_a_b = (len(df1['fico'] > 700)/len(df)) / p_a
result = (p_a_b == p_b)
print(result)
# code ends here


# --------------
# code starts here
prob_lp = len(df[df['paid.back.loan'] == 'Yes']) / len(df) #p(A)
prob_cs = len(df[df['credit.policy'] == 'Yes']) / len(df) #p(B)
new_df = df[df['paid.back.loan'] == 'Yes']
prob_pd_cs = (len(new_df[new_df['credit.policy'] == 'Yes'])/len(df)) / prob_lp  #p(B|A)
bayes =  (prob_pd_cs * prob_lp) / prob_cs  #p(A|B)
print(bayes)
# code ends here


# --------------
# code starts here
df1 = df[df['paid.back.loan'] == 'No']
df1['purpose'].value_counts().plot(kind='bar', figsize=(15,12))
# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()
fig, (ax_1, ax_2) = plt.subplots(nrows=1, ncols=2, figsize=(15,6))
df['installment'].hist(ax=ax_1, color='green')
ax_1.vlines(x=inst_median, colors='yellow', ymin=0, ymax=2500, label='median', linestyles ='dashed')
ax_1.vlines(x=inst_mean, colors='red', ymin=0, ymax=2500, label='mean', linestyles ='solid')
ax_1.legend()
ax_1.set_title('Installments')
df['log.annual.inc'].hist(ax=ax_2, color='orange')
ax_2.set_title('Log of Annual Income')
plt.show();
# code ends here


