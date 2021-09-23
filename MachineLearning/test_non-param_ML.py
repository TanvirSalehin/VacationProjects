#	Gini Impurity = 2 * p * (1 - p)		Here, p is the percent of succes in spliting.
#										What I mean is say 20% people survived in an accident. So, p will be 0.2
#	Entropy
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



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import graphviz
from sklearn import linear_model, metrics, model_selection, tree
from IPython.display import Image
#from sklearn.linear_model import LogisticRegression
#from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
#from sklearn.metrics import confusion_matrix, precision_recall_fscore_support, roc_curve
#from sklearn.model_selection import train_test_split, KFold
#from sklearn.tree import export_graphviz

'''
    df = pd.read_csv("titanic.csv")
    df["male"] = df["Sex"] == "male"
    X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']][:800].values
    y = df["Survived"][:800].values
    n_split = 5
    kf = model_selection.KFold(n_splits = n_split, shuffle = True, random_state = 88)
    
    for criterion in ["gini", "entropy"]:
        accuracy = []
        precision = []
        recall = []
        f1 = []
        for train_kf, test_kf in kf.split(X):
            X_train_kf, y_train_kf = X[train_kf], y[train_kf]
            X_test_kf, y_test_kf = X[test_kf], y[test_kf]
    
            dt = tree.DecisionTreeClassifier(criterion = criterion, random_state = 2988)
    
            dt.fit(X_train_kf, y_train_kf)
    
            y_pred_kf = dt.predict(X_test_kf)
    
            accuracy.append(metrics.accuracy_score(y_test_kf, y_pred_kf))
            precision.append(metrics.precision_score(y_test_kf, y_pred_kf))
            recall.append(metrics.recall_score(y_test_kf, y_pred_kf))
            f1.append(metrics.f1_score(y_test_kf, y_pred_kf))
    
        print(f"----- {criterion} -----")
        print()
        print("Accuracy: ", np.mean(accuracy))
        print("Precision: ", np.mean(precision))
        print("Recall: ", np.mean(recall))
        print("F1 Score: ", np.mean(f1))
        print()
    
    accuracy = []
    precision = []
    recall = []
    f1 = []
    for train_kf, test_kf in kf.split(X):
        X_train_kf, y_train_kf = X[train_kf], y[train_kf]
        X_test_kf, y_test_kf = X[test_kf], y[test_kf]
    
        model = linear_model.LogisticRegression(random_state = 2988)
    
        model.fit(X_train_kf, y_train_kf)
    
        y_pred_kf = model.predict(X_test_kf)
    
        accuracy.append(metrics.accuracy_score(y_test_kf, y_pred_kf))
        precision.append(metrics.precision_score(y_test_kf, y_pred_kf))
        recall.append(metrics.recall_score(y_test_kf, y_pred_kf))
        f1.append(metrics.f1_score(y_test_kf, y_pred_kf))
    
    print("----- Logistic Regression -----")
    print()
    print("Accuracy: ", np.mean(accuracy))
    print("Precision: ", np.mean(precision))
    print("Recall: ", np.mean(recall))
    print("F1 Score: ", np.mean(f1))
    print()
'''


df = pd.read_csv("titanic.csv")
df["Male"] = df["Sex"] == "male"
feature_names = ['Pclass', 'Male', 'Age', 'Fare']
X = df[feature_names].values
y = df["Survived"].values

dt = tree.DecisionTreeClassifier(criterion = "entropy")
dt.fit(X, y)
dot_file = tree.export_graphviz(dt, feature_names=feature_names)
graph = graphviz.Source(dot_file)
graph.render(filename='tree', format='png', cleanup=True)


