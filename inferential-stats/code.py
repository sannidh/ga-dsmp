# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings
warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000
#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  
# path        [File location variable]
data = pd.read_csv(path)
#Code starts here
data_sample = data.sample(n=sample_size, random_state=0)
sample_mean = data_sample['installment'].mean()
sample_std = data_sample['installment'].std()
margin_of_error = z_critical * sample_std / (sample_size)**0.5
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
true_mean = data['installment'].mean()
if confidence_interval[0] <= true_mean <= confidence_interval[1]:
    print('True mean falls within CI')


# --------------
import matplotlib.pyplot as plt
import numpy as np
#Different sample sizes to take
sample_size=np.array([20,50,100])
#Code starts here
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(15, 21))
m = []
for i in range(len(sample_size)):
    for j in range(1000):
        sample_data = data.sample(n = sample_size[i])
        m.append(sample_data['installment'].mean())
    mean_series = pd.Series(m)
    mean_series.plot.hist(ax=axes[i])
    plt.xlabel('Installments')


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest
#Code starts here
data['int.rate'] = data['int.rate'].map(lambda x:x.rstrip('%')).astype('float')/100
z_statistic, p_value = ztest(data[data['purpose']=='small_business']['int.rate'], 
                             value=data['int.rate'].mean(), alternative='larger')
if p_value < 0.05:
    inference = 'The interest rate for small businesses is greater than others'
else:
    inference = 'The interest rate for small businesses is not different to others'
print(inference)


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest
#Code starts here
z_statistic, p_value = ztest(x1=data[data['paid.back.loan']=='No']['installment'], 
                             x2=data[data['paid.back.loan']=='Yes']['installment'], alternative='two-sided')
if p_value < 0.05:
    inference = 'The installments for defaulters is different than others'
else:
    inference = 'The installments for defaulters is NOT different than others'
print(inference)


# --------------
#Importing header files
from scipy.stats import chi2_contingency
#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1
#Code starts here
critical_value = stats.chi2.ppf(q=0.95, df=6)
yes = data[data['paid.back.loan'] =='Yes']['purpose'].value_counts()
no = data[data['paid.back.loan']=='No']['purpose'].value_counts()
observed = pd.concat([yes.transpose(),no.transpose()], axis=1, keys=['Yes', 'No'], sort=True)
chi2, p, dof, ex = chi2_contingency(observed)
if chi2 > critical_value:
    inference = 'The purpose of loan has an impact on defaults'
else:
    inference = 'The purpose of loan has NO impact on defaults'
print(inference)


