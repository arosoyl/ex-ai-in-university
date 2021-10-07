import pandas as pd
import numpy as np
import matplotlib.pyplot as plr

#Logistic
from networkx.drawing.tests.test_pylab import plt

data= pd.read_csv('logistic.csv',header=None)
#print(data)
print(data.values)
true_x = []
true_y = []
false_x = []
false_y = []
for item in data.values:
    if item[2] == 1. :
        true_x.append(item[0])
        true_y.append(item[1])
    else:
        false_x.append(item[0])
        false_y.append(item[1])

plt.scatter(true_x,true_y, marker ='o', color ='b')
plt.scatter(false_x,false_y, marker ='s', color ='r')
plt.show()

def sigmoid(z):
    return 1.0/ (1 + np.exp(-z))

def phan_chia(p):
    if p >= 0.5:     return 1
    else: return 0

def predict(feature, weights):
    z = np.dot(feature, weights)
    return sigmoid(z)
def cost_function(features,labels,weights):
    """

    :param features:
    :param labels:
    :param weights:
    :return: chi phi cost
    """
    n = len(labels)
    predictions = predict (features, weights)

    cost_class1 = - labels * np.log(predictions)
    cost_class2 = - (1-labels)*np.log(1 - predictions)

    cost = cost_class1 + cost_class2
    return cost.sum()/n

def update_weight(features, labels, weights, learning_rate):

    """

    :param features:
    :param labels:
    :param weights:
    :param learning_rate:
    :return:
    """
    n = len(labels)

    predictions = predict(features,weights)
    gd = np.dot(features.T, (predictions - labels))
    gd = gd/n
    gd = gd * learning_rate
    weight = weights - gd
    return weights

