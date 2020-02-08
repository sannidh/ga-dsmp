### Project Overview

 Predict prices using Melbourne housing data using regularized regression. Each observation is a different house attribute with various features, like the number of properties that exist in the suburb, land size, building size, governing council for the area, real estate agent, price of the house, etc.
Some features like Type, Method, SellerG, CouncilArea, and Regionname in the data are textual in nature, which will be converted into nominal values. Other variables like rooms, price, distance etc are numerical.
Finally building a regularized regression model with the following applications

1. Train-test split
2. Correlation between the features
3. Linear Regression
4. Polynomial Regressor
5. Lasso Regressor
6. Ridge Regressor
7. R-squared evaluation metrics


### Learnings from the project

 - Predicting the price of the house using linear regression.
- Using a lasso regressor. Check if there is any improvement in the prediction
- There wasn't a clear improvement after applying the lasso regressor; that once again drives home the point that it's not necessary that the model will improve after regularization.
- Using cross-validated estimators to predict house prices. Choosing estimators and their parameters.
- There is very less improvement(~1%), even after applying the regularization and cross-validation score. It shows a improvement in test prediction using a polynomial regressor to generate second-degree polynomial features.


