The data file is in main code folder named: "yelp_academic_dataset_business.json"

Please run the code file "235 Naive Bayes.ipynb" with Jupyter Notebook. Make sure the data file and code file are under the same folder.

Part of pre-processing code is helped from http://jasontdean.com/python/Yelp.html
 
I firstly pre-precessed the raw data to a dataframe with 9 attributes: alcohol, bike parking, business parking, good for kids, has TV, outdoor seating, restaurant attire, restaurants reservations and WiFi. Separate star ratings to 2 classes: high rating: stars >= 4 and low rating: stars < 4. Then I separated the data to training and test with ratio of 9:1. 

I used the SKlearn package of Naive Bayes to test the data. After making sure the data is good to work on, I implemented the Naive Bayes classifier from scratch. First I built function NaiveBayesTrain(trainX,trainY) to train the data and calculate the probabilities of each attribute given class and the class probability. Second I built NaiveBayesTest(trainX,trainY,testX) to return target value based on the test data. Finally I used accuracy_score(Y_test,Y_pred) to calculate the accuracy of this classifier on predicting star ratings based on attributes.