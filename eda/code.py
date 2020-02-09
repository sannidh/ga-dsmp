# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Code starts here
data = pd.read_csv(path)
data = data[data['Rating'] <= 5]
data['Rating'].plot(kind='hist')
#Code ends here


# --------------
# code starts here
total_null = data.isnull().sum()
percent_null = total_null/data.isnull().count()
missing_data = pd.concat([total_null, percent_null], axis=1, keys=['Total', 'Percent'])
print(missing_data)
data.dropna(inplace=True)
total_null_1 = data.isnull().sum()
percent_null_1 = total_null_1/data.isnull().count()
missing_data_1 = pd.concat([total_null_1, percent_null_1], axis=1, keys=['Total', 'Percent'])
print(missing_data_1)
# code ends here


# --------------
#Code starts here
sns.catplot(x='Category', y='Rating', data=data, kind='box', height=10)
plt.xticks(rotation=90)
plt.title('Rating vs Category [BoxPlot]')
#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
#Code starts here
print(data['Installs'].value_counts())
data['Installs'] = data['Installs'].map(lambda x: x.rstrip('+'))
data['Installs'].replace(to_replace=r',',value='',inplace=True, regex=True)
data[['Installs']] = data[['Installs']].astype('int')
le = LabelEncoder()
data['Installs'] = le.fit_transform(data['Installs'])
sns.regplot(x='Installs', y='Rating', data=data)
plt.title('Rating vs Installs [RegPlot]')
#Code ends here


# --------------
#Code starts here
print(data['Price'].value_counts())
data['Price'] = data['Price'].map(lambda x: x.lstrip('$'))
data[['Price']] = data[['Price']].astype('float')
sns.regplot(x='Price', y='Rating', data=data)
plt.title('Rating vs Price [RegPlot]')
#Code ends here


# --------------
#Code starts here
data['Genres'].unique()
data['Genres'] = data['Genres'].map(lambda x: x.split(';')[0])
gr_mean = data.groupby(['Genres'], as_index=False).agg({'Rating':'mean'})
gr_mean.describe()
gr_mean = gr_mean.sort_values('Rating')
print(gr_mean.iloc[0,:])
print(gr_mean.iloc[-1,:])
#Code ends here


# --------------
#Code starts here
print(data['Last Updated'])
data['Last Updated'] = pd.to_datetime(data['Last Updated'])
max_date = data['Last Updated'].max()
data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days
sns.regplot(x="Last Updated Days", y="Rating", data=data)
#Code ends here


