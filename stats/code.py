# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#path of the data file- path
#Code starts here 
data = pd.read_csv(path)
data['Gender'].replace('-', 'Agender', inplace=True)
gender_count = data['Gender'].value_counts()
gender_count.plot(kind='bar')


# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
alignment.plot(kind='pie')
plt.ylabel('Character Alignment')


# --------------
#Code starts here
sc_df = data[['Strength', 'Combat']]
sc_covariance = sc_df.cov().iloc[0,1]
sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()
sc_pearson = sc_covariance/(sc_strength * sc_combat)
ic_df = data[['Intelligence', 'Combat']]
ic_covariance = ic_df.cov().iloc[0,1]
ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()
ic_pearson = ic_covariance/(ic_intelligence * ic_combat)


# --------------
#Code starts here
total_high = data['Total'].quantile(0.99)
super_best = data[data['Total'] > total_high]
super_best_names = list(super_best['Name'])
print('The super best superheroes are: ', super_best_names)


# --------------
#Code starts here
import seaborn as sns
fig, (ax_1, ax_2, ax_3) = plt.subplots(nrows=1, ncols=3, figsize=(12,12))
sns.boxplot(y=super_best['Intelligence'], ax=ax_1, color='yellow')
ax_1.set_title('Intelligence')
sns.boxplot(y=super_best['Speed'], ax=ax_2, color='orange')
ax_2.set_title('Speed')
sns.boxplot(y=super_best['Power'], ax=ax_3, color='green')
ax_3.set_title('Power')
plt.show();


