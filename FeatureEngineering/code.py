# --------------
import pandas as pd
from sklearn import preprocessing
#path : File path
# Code starts here
# read the dataset
dataset = pd.read_csv(path)
# look at the first five columns
print(dataset.head(5))
# Check if there's any column which is not useful and remove it like the column id
print('\nMissing Columns: \n')
print(dataset.isnull().sum())
dataset.drop(columns='Id', inplace=True)
# check the statistical description
print('\nStatistical Information: \n')
print(dataset.describe())


# --------------
# We will visualize all the attributes using Violin Plot - a combination of box and density plots
import seaborn as sns
from matplotlib import pyplot as plt
#names of all the attributes 
cols = list(dataset.columns)
#number of attributes (exclude target)
size = dataset.shape[1]-1
#x-axis has target attribute to distinguish between classes
x = dataset['Cover_Type']
#y-axis shows values of an attribute
y = dataset.drop(columns='Cover_Type')
#Plot violin for all attributes
fig = plt.figure(figsize=(30,80))
for n in range(size):
    ax = fig.add_subplot(18,3,n+1)
    sns.violinplot(x, y.iloc[:,n], ax=ax)
plt.tight_layout()
plt.show()


# --------------
upper_threshold = 0.5
lower_threshold = -0.5
# Code Starts Here
subset_train = dataset.iloc[:,:10]
data_corr = subset_train.corr(method='pearson')
plt.figure(figsize=(15,8))
sns.heatmap(data_corr, annot=True, cmap='magma', linewidths=0.5)
correlation = data_corr.unstack().sort_values(kind='quicksort')
corr_var_list = correlation[((correlation>upper_threshold)|(correlation<lower_threshold))&(correlation!=1)]
# Code ends here


# --------------
#Import libraries 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# Identify the unnecessary columns and remove it 
dataset.drop(columns=['Soil_Type7', 'Soil_Type15'], inplace=True)
# Scales are not the same for all variables. Hence, rescaling and standardization may be necessary for some algorithm to be applied on it.
X = dataset.drop(columns='Cover_Type')
Y = dataset['Cover_Type']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
#Standardized
scaler = StandardScaler()
#Apply transform only for continuous data
X_train_temp = pd.DataFrame(scaler.fit_transform(X_train.iloc[:,:10]), columns=X_train.iloc[:,:10].columns)
X_test_temp = pd.DataFrame(scaler.transform(X_test.iloc[:,:10]), columns=X_test.iloc[:,:10].columns) 
#Concatenate scaled continuous data and categorical
X_train_temp.index = X_train.index
X_test_temp.index = X_test.index
X_train1 = pd.concat([X_train_temp, X_train.iloc[:,10:]], axis=1)
X_test1 = pd.concat([X_test_temp, X_test.iloc[:,10:]], axis=1)
scaled_features_train_df = X_train1
scaled_features_test_df = X_test1


# --------------
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import f_classif
# Write your solution here:
skb = SelectPercentile(score_func = f_classif, percentile=90)
predictors = skb.fit_transform(X_train1, Y_train)
scores = skb.scores_
Features = X_train1.columns
dataframe = pd.DataFrame({'Features':Features, 'scores':scores})
dataframe.sort_values('scores', ascending=False, inplace=True)
top_k_predictors = list(dataframe[dataframe.scores >= dataframe.scores.quantile(0.1)].Features)
print(top_k_predictors)


# --------------
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score
clf = OneVsRestClassifier(estimator=LogisticRegression())
clf1 = OneVsRestClassifier(estimator=LogisticRegression())
model_fit_all_features = clf1.fit(X_train, Y_train)
predictions_all_features = model_fit_all_features.predict(X_test)
score_all_features = accuracy_score(Y_test, predictions_all_features)
print("Accuracy Score for All Features: ", score_all_features)
model_fit_top_features = clf.fit(scaled_features_train_df[top_k_predictors], Y_train)
predictions_top_features = clf.predict(scaled_features_test_df[top_k_predictors])
score_top_features = accuracy_score(Y_test, predictions_top_features)
print("Accuracy Score for Top Scaled Features: ", score_top_features)


