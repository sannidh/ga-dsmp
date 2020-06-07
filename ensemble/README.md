### Project Overview

 **Mars Crater - Problem statement**
Determine if the instance is a crater or not a crater. 1=Crater, 0=Not Crater Using the technique described by L. Bandeira (Bandeira, Ding, Stepinski. 2010. Automatic Detection of Sub-km Craters Using Shape and Texture Information) we identify crater candidates in the image using a pipeline. Each crater i.e a candidate image block is normalized to a standard scale of 48 pixels. Each of the nine kinds of image masks probes the normalized image block in four different scales of 12 pixels, 24 pixels, 36 pixels, and 48 pixels, with a step of a third of the mask size (meaning 2/3 overlap). We totally extract 1,090 Haar-like attributes using nine types of masks as the attribute vectors to represent each crater candidate. The dataset was converted to the Weka ARFF format by Joseph Paul Cohen in 2012.

- [ ] We import image from the Matplotlib library as mpimg.
- [ ] Use mpimg.imread to read the image as numpy as array.


### Approach taken to solve the problem

 - Loading the data and using a MinMaxScaler to transform data of the 1090 Haar-like attributes of the images of mars crater
- Check the roc_auc_score after building the first ML model - a simple logistic regression - 0.82952
- Check the efficacy of a decision tree and a random forest on the same dataset - 0.87328 & RF - 0.93316
- Use Bagging Classifier or bootstrap aggregation to pass 100 Decision Trees to see increase in accuracy of prediction - 0.832579
- Using VotingClassfier to do naive aggregation of multiple ML models tested in the preceding steps - 0.92081


