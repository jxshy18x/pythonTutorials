import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.model_selection import cross_val_score,KFold

#1, import iris.csv
data = pd.read_csv("iris.csv")

#2, view first 4 records
print(data.head(4))

#3, create input attributes (X) and outcome values (Y) from data set
d = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
data['species'] = data['species'].map(d)

X = data.drop('species', axis=1)  # input attributes (sepal/petal measurements)
y = data['species']               # outcome values (0, 1, or 2)

print(X.head())
print(y.head())

#4, split data into a training set (80%) and test set (20%)
xTrain,xTest,yTrain,yTest =train_test_split(X,y,test_size=0.20)

#5, fit training data and build decision tree classifier
decisionTree = DecisionTreeClassifier()
decisionTree.fit(xTrain, yTrain)

#6, determine accuracy of predictions of test set
yPred = decisionTree.predict(xTest)
print("Accuracy", metrics.accuracy_score(yTest, yPred))

#7, determine accuracy of predictions of training set explain
yPred = decisionTree.predict(xTrain)
print("Accuracy:",metrics.accuracy_score(yTrain, yPred))

#8, display decision tree
fig, axes = plt.subplots(nrows = 1, ncols = 1, figsize = (4,3), dpi = 300)
tree.plot_tree(decisionTree, feature_names = ["sepal_length", "sepal_width", "petal_length", "petal_width"],
class_names = ["0", "1", "2"], filled = True)
fig.savefig('imagename.png')

#9, optimisation of decision
decisionTree1 = DecisionTreeClassifier(criterion="entropy", max_depth=3, min_samples_split=6, min_samples_leaf=6)
decisionTree1.fit(xTrain, yTrain)
yPred = decisionTree1.predict(xTest)
print("Accuracy:", metrics.accuracy_score(yTest, yPred))

#10, determine accuracy of model using kfold valdiation to evaluat the dt classifier

#max_depth=1
dt11=DecisionTreeClassifier(criterion='entropy',max_depth=1)
dt11.fit(xTrain,yTrain)
yPred = dt11.predict(xTest)
print("Accuracy:",metrics.accuracy_score(yTest, yPred))

#max_depth=2
dt12=DecisionTreeClassifier(criterion='entropy',max_depth=2)
dt12.fit(xTrain,yTrain)
yPred = dt12.predict(xTest)
print("Accuracy:",metrics.accuracy_score(yTest, yPred))

#max_depth=3
dt13=DecisionTreeClassifier(criterion='entropy',max_depth=3)
dt13.fit(xTrain,yTrain)
yPred = dt13.predict(xTest)
print("Accuracy:",metrics.accuracy_score(yTest, yPred))

#max_depth=4
dt14=DecisionTreeClassifier(criterion='entropy',max_depth=4)
dt14.fit(xTrain,yTrain)
yPred = dt14.predict(xTest)
print("Accuracy:",metrics.accuracy_score(yTest, yPred))


# In[130]:


#max_depth=5
dt15=DecisionTreeClassifier(criterion='entropy',max_depth=5)
dt15.fit(xTrain,yTrain)
yPred = dt15.predict(xTest)
print("Accuracy:",metrics.accuracy_score(yTest, yPred))

dt14=DecisionTreeClassifier(criterion='entropy',max_depth=4, min_samples_split=5,min_samples_leaf = 5,)
dt14.fit(xTrain,yTrain)
yPred = dt14.predict(xTest)
print("Accuracy:",metrics.accuracy_score(yTest, yPred))

kf = KFold(n_splits=5)
score = cross_val_score(decisionTree, X, y, cv = kf)
print(score.mean())