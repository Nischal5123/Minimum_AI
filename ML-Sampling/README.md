k-nearest neighbors (k-NN) is a very popular and long-used algorithm for supervised learning.
Given a set of labeled data points, the objective is to determine the label of a new, test, point.
k-NN does that by first finding the k points in the data set that are nearest the test point.
It then determines which label appears most often in these k nearest neighbors. The test point is assigned that label.

For instance, if k=3, and the 3 nearest points have labels Red, Red and Orange, the test point is labeled Red. 


Distribution of Points in KNN