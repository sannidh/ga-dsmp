### Project Overview

 Google Play Store serves as the official app store for the Android operating system, allowing users to browse and download applications. Success of an app is largely determined by its ratings.

1. We will check if the there is a particular pattern among highly rated apps.
2. Secondly if app features like size or genre play a role in the final rating!
3. We will remove missing values, clean the data & do EDA on the dataset to form hypothesis to test later
4. The dataset has details of 10841 apps with 13 features


### Approach taken to solve the problem

 **Perform EDA on the target variable i.e rating**
- It can be seen that the target is greater than 5 at places with some NaN values
- Subsetting the data with the acceptable rating range i.e 0-5 will remove NaN values

**Null Value or Missing Observation Treatment**
- Calculating percentage of null values of each feature
- Dropping observations/rows with null values

**Category vs Rating**
- Checking whether category and ratings have any sort of relation
- From the boxplot it seems ratings do not vary by category of app

**Data Transformation**
- Cleaning Installs feature with label encoder since it does not have int values and range is 0-1 Bn with commas
- Transforming with labelencoder to reduce the range of numerical values
- Using regression plot for Installs vs Rating to check the power of the feature

**Checking the impact of Price with Ratings, we see that:**
- A negative correlation between price and ratings
- Higher price applications may make customers disappointed if they are not good enough.

**Genres vs Rating**
- Cleaning the Genres columns

**Last Updated vs Rating**
- Visualizing the recency of updates with rating
- Transforming the updation values to datetime format
- We observe that the number of days since updation affect the rating in inverse manner


