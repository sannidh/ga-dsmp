### Project Overview

 Prediction of the **forest cover type** (the predominant kind of tree cover) from strictly cartographic variables (as opposed to remotely sensed data)

The study area includes four wilderness areas located in the Roosevelt National Forest of northern Colorado. Each observation is a 30m x 30m patch. You are asked to predict an integer classification for the forest cover type. The seven classifier types are:

1. Spruce/Fir 
2. Lodgepole Pine 
3. Ponderosa Pine 
4. Cottonwood/Willow 
5. Aspen 
6. Douglas-fir 
7. Krummholz

It contains 55 features including dummy variables for categorical data and 15120 observations.


### Approach taken to solve the problem

 **Exploratory Data Analysis**

- [ ] **Violin Plots** for all variables wrt Target variable helps find the important features
- [ ] Elevation is has a separate distribution for most classes. Seems highly correlated with the target and hence an important attribute
- [ ] Aspect contains a couple of normal distribution for several classes
- [ ] Horizontal distance to road and hydrology have a similar distribution
- [ ] Lots of 0s in the vertical distance to hydrology
- [ ] Wilderness_Area3 gives no class distinction
- [ ] As values are not present, others give some scope to distinguish Soil_Type, 1,5,8,9,12,14,18-22, 25-30 and 35-40 offer class distinction as values are not present for many classes

**Relationship between different variables**

- [ ] We use the heatmap from seaborn to look at the correlation between continuous features
- [ ] And we will filter the pairwise factors with absolute correlations greater than 0.5.

**Data preprocessing for feature selection**

- [ ] Using cross validation & scaling continuous data using standard scaler
- [ ] Separating data into training and test data

**Feature Selection using Select percentile**

- [ ] Using f_classifier or ANOVA to select a set of meaningful features
- [ ] Transforming the train dataset and retrieving the top 90 percentile features & score list
- [ ] We observe that the top 90 percentile features basis an ANOVA test leaves out 6 features

**Effect of feature selection on model prediction**

- [ ] Testing with OneVsRestClassifier and a logistic regression classifier
- [ ] Running the predictions with top 90 percentile features based on the ANOVA test (f-classifier)
- [ ] Also testing with scaled features vs unscaled features, we observe that the accuracy score goes up by 10%


