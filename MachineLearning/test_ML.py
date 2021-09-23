#sklearnTut

    #   Logistic Regression, while it has regression in its name is an algorithm for solving classification problems, not regression problems.
    #	A line is drawn with the equation    0 = ax + by + c    which separates the 2 classes of values.
    #   Area Under the Curve, also called the AUC, is the area under the ROC curve. It’s a value between 0 and 1, the higher the better.
    #   LogisticRegression class: fit (to train the model), score (to calculate the accuracy score) and predict (to make predictions).
    #
    #-------------------------------------------------------------------------------------------------------------------#
    #
    # *	from sklearn.linear_model import LogisticRegression
    #
    #	model = LogisticRegression()	To initiate
    #	model.fit(X, y)					It takes two arguments: X (the features as a 2d numpy array) and y (the target as a 1d numpy array).
    #	model.coef_, model.intercept_ 	returns the [a, b] and [c] coefficients respectively.
    #	model.predict(X)				Takes X (the features as a 2d numpy array) and returns the prediction of y (the target as a 1d numpy array).
    #	model.score(X, y)				return a value between 0 and 1. This is the accuracy of the prediction.
    #	
    #
    # *	from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, roc_auc_score
    #
    #	accuracy_score(), precision_score(), recall_score(), f1_score()
    #		Each function takes two 1-dimensional numpy arrays: the true values of the target & the predicted values of the target.
    #
    #	roc_curve(y_test, y_pred_proba[:,1])	returns an array of the false positive rates, an array of the true positive rates and the thresholds.
    #
    #   roc_auc_score(y_test, y_pred_proba[:,1])    returns the area under the ROC. Value is between 1 and 0. The more, the better
    #
    #	model.confusion_matrix(True_Value_of_Target, Predicted_Value_of_Target)		returns the confusion matrix [[TN, FP], [FN, TP]]
    #
    #
    # * from sklearn.model_selection import train_test_split, KFold
    #
    #	train_test_split(X, y)		      returns 4 values: X_train, X_test, y_train, y_test (Train means for training. Test means for testing.)
    #									  Optional parameter	:	train_size = x  	0 < x < 1		Suppose x is 0.6, so 60% data will be sent for training and 40% for testing. By default it is 0.75
    #									  						    random_state = x 	x : any number	This will cause the scores to be same everytime. It is also called seed.	
    #
    #	kf = KFold(n_splits=3, shuffle=True)      initiating the KFold class object.
    #       kf.split(X)                    Takes X (the features as a 2d numpy array) and returns a generator of 2 lists, first one being for training and 2nd one for testing.
    #
    #
    #
    #	TP 	 - 	 True Positives						-	Correct Prediction
    #	FP 	 - 	 False Positive (Real Negative)		-	Wrong Prediction
    #	FN 	 - 	 False Negative (Real Positive)		-	Wrong Predition
    #	TN 	 - 	 True Negative						-	Correct Predction
    #
    #	Precision 	- 	TP / (TP + FP) 	 - 	TP out of all Predicted Positives
    #	Sensitivity	=	Recall
    #	Recall 		- 	TP / (TP + FN) 	 - 	TP out of all Real Positives
    #	Specificity	-	TN / (TN + FP)	 -	TN out of all Real Negatives
    #
    #	F1 Score -->	2 * (Precision * Recall) / (Precision + Recall)
    #
#========================================================================================================================#
#pltTut
    #   NEVER FORGET TO USE plt.show() AT THE END.
    #
    #   plt.scatter(x, y)     First argument is x-axis, second is y-axis. x and y are lists.
    #	plt.xlabel("Label")   Label in x-axis.
    #	plt.ylabel("Label")   Label in y-axis.
    #	plt.plot([x1, x2], [y1, y2])   Draws a line from [x1, y1] to [x2, y2].
    #
    #	
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
#========================================================================================================================#
#pandasTut

    #   Table of data or Pandas data object is called DataFrame.
    #   Search in google --
    #   Mask, 
    #   Classification, Regression, Supervised and Unsupervised learning, Target, Logistic Regression, Feature / Predictors, Confusion Matrix 
    #
    #---------------------------------------------------------------------------------------------------------------------------#
    #
    #   Useful Things.
    #
    #   1.  pandas.read_csv("something.csv")      Takes a file in csv format and converts it to a Pandas DataFrame.
    #              The object returned has few methods.
    #
    #               1.  head(n = 5)               returns n rows, by default 5 rows.
    #				2.  describe()                returns few useful statistics about the data --> count, mean, std, min, max, percentile
    #				3.  object["ColumnName"]      returns the column, which is called the Pandas Series. Series is a DataFrame but only a single column.
    #				4.  object[["Column1, Column2..., ColumnN"]]   returns N columns. MUST USE DOUBLE SQUARE BRACKETS.
    #
    #				5.  object["NewCol"] = object["ExistingCol"] + SomeOperation   -->   Makes a new column such that the values of the new column correspond
    #																					 to another existing column.
    #																					 Suppose there is a column of "Gender". We want to make a new column
    #																					 named "Male" whose values will be True if corresponding value in "Gender"
    #																					 is "male" and False if "female". Syntax will be
    #																					 object["Male"] = object["Gender"] == "male"
    #				
    #				6.  object["Column"].values   returns the values as a numpy array.
    #				7.  object[["Column1", "Column2"..., "ColumnN"]].values   returns numpy array as a 2 dimensional array. Each array in the 2 dimensional array
    #																		  contains values from each column given in the syntax. Run the code to see how it works.
    #
    #				8.  NumpyArray.shape or obejct.shape   returns a tuple of rows and columns. row is pashapashi, column is upor-niche. :) (Amr mone thake na)
    #				9.  npArray[2, 1]   What you would expect to return. The 2nd element of the 3rd list/row.
    #				10. npArray[1]      The 2nd row is returned.
    #				11. npArray[:,2]    The 3rd column is returned
    #               12. npArr[npArr[:,2] < 18]   Selects all the rows which have their 3rd element less than 18. (Google: Mask)
    #				13. (npArr[:,0] != "Tanvir").sum()   return the number of rows which do not have "Tanvir" as their 1st element.
    #				14. npArr[:2]		The first 2 rows are returned
    #
    #
#========================================================================================================================#
#NumPyTut

    #    List or table of data in numpy is called numpy array.
    #    It’s standard practice to call our 2d array of features X and our 1d array of target values y.
    #
    #
    #   Things that I don't know.
    #
    #   Variance:
    #     We take the mean of the data, calculate how far each value is from the mean (subtract them),
    #     square each far-value and add them, divide by the number of values.
    #
    #   Standard Deviation:
    #     Root of the Varance of a given data.
    #
    #   Percentile:
    #     The median can also be thought of as the 50th percentile. Example on the data below.
    #     data = [15, 16, 18, 19, 22, 24, 29, 30, 34]
    #	  50th percentile of the data is 22
    #	  We have 9 values, so 25% of the data would be approximately 2 datapoints.
    #	  So the 3rd datapoint is greater than 25% of the data. Thus, the 25th percentile is 18 (the 3rd datapoint).
    #	  Similarly, 75% of the data is approximately 6 datapoints. So the 7th datapoint is greater than 75% of the data.
    # 	  Thus, the 75th percentile is 29 (the 7th datapoint).

    #----------------------------------------------------------------------------------------------------------------------#

    #   Useful Things.
    #
    #   numpy.mean(data)                Mathematical mean.
    #   numpy.median(data)              Median of the data.
    #   numpy.percentile(data, n)       The nth percentile of the data.
    #   numpy.std(data)                 Standard deviation of the data.
    #   numpy.var(data)                 Variance of the data.
    #
    #   data --> a list of datas --> [1, 2, 5, 12, 33, 34, 37, 41, 54, 32]
    #   n --> any number between 0 and 100
#========================================================================================================================#


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support, roc_curve
from sklearn.model_selection import train_test_split, KFold

model = LogisticRegression()
df = pd.read_csv('titanic.csv')
df["male"] = df["Sex"] == "male"
X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y = df["Survived"].values
sensitivity_score = recall_score
def specificity_score(y_true, y_pred):
    p, r, f, s = precision_recall_fscore_support(y_true, y_pred)
    return r[0]



X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)
fpr, tpr, threshold = roc_curve(y_test, y_pred_proba[:,1])




X_train2, X_test2, y_train2, y_test2 = train_test_split(X, y, train_size = 0.5)
model.fit(X_train2, y_train2)
y_pred2 = model.predict(X_test2)
y_pred_proba2 = model.predict_proba(X_test2)
fpr2, tpr2, threshold2 = roc_curve(y_test2, y_pred_proba2[:,1])



'''
    plt.plot(fpr, tpr)
    plt.plot(fpr2, tpr2)
    plt.plot([0, 1], [0, 1], linestyle = "--")
    plt.xlabel("1 - Specificity")
    plt.ylabel("Sensitivity")
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])

    plt.show()
'''
'''
    X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']][:800].values
    y = df["Survived"][:800].values

    n_split = 5
    kf = KFold(n_splits = n_split, shuffle = True)
    splits = kf.split(X)

    accuracy = 0
    precision = 0
    recall = 0
    specificity = 0
    f1 = 0

    for train_kf, test_kf in splits:

        X_train_kf = X[train_kf]
        X_test_kf = X[test_kf]
        y_train_kf = y[train_kf]
        y_test_kf = y[test_kf]

        model.fit(X_train_kf, y_train_kf)

        y_prob_kf = model.predict(X_test_kf)

        accuracy_kf = accuracy_score(y_test_kf, y_prob_kf)
        precision_kf = precision_score(y_test_kf, y_prob_kf)
        recall_kf = recall_score(y_test_kf, y_prob_kf)
        specificity_kf = specificity_score(y_test_kf, y_prob_kf)
        f1_kf = f1_score(y_test_kf, y_prob_kf)

        accuracy += accuracy_kf
        precision += precision_kf
        recall += recall_kf
        specificity += specificity_kf
        f1 += f1_kf

    print(" Accuracy: ", accuracy / nsplit, "\n", "Precision: ", precision / nsplit, "\n", "Recall: ", recall / nsplit, "\n", "Specificity: ", specificity / nsplit, "\n", "F1 Score: ", f1 / nsplit)
'''



