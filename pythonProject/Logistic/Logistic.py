import csv

import numpy as np
import matplotlib.pyplot as plt
def prod(w,X):
    return np.dot(w.T, X)
def sigmoid(s):
    return 1/(1 + np.exp(-s))
def my_logistic_sigmoid_regression(X, y, w_init, eta, epsilon = 1e-3, M = 10000):
    w = [w_init]
    N = X.shape[1]
    d = X.shape[0]
    count = 0
    check_w_after = 20
    while count < M:
        # mix data
        mix_id = np.random.permutation(N)
        for i in mix_id:
            xi = X[:, i].reshape(d, 1)
            yi = y[i]
            zi = sigmoid(np.dot(w[-1].T, xi))
            w_new = w[-1] + eta*(yi - zi)*xi
            count += 1
            # stopping criteria
            if count % check_w_after == 0:
                if np.linalg.norm(w_new - w[-check_w_after]) < epsilon:
                    return w
            w.append(w_new)
    return w
def display(w,X,y):
    X0 = X[1, np.where(y == 0)][0]
    y0 = y[np.where(y == 0)]
    X1 = X[1, np.where(y == 1)][0]
    y1 = y[np.where(y == 1)]
    plt.plot(X0, y0, 'ro', markersize=8)
    plt.plot(X1, y1, 'bs', markersize=8)
    xx = np.linspace(0, 6, 1000)
    w0 = w[-1][0][0]
    w1 = w[-1][1][0]
    threshold = -w0 / w1
    yy = sigmoid(w0 + w1 * xx)
    yy1 = sigmoid(w0 + w1 * 3.8)
    plt.axis([-2, 8, -1, 2])
    plt.plot(xx, yy, 'g-', linewidth=2)
    plt.plot(3.8, yy1, 'y^', markersize=8)
    plt.plot(threshold, .5, 'y^', markersize=8)
    plt.xlabel('studying hours')
    plt.ylabel('predicted probability of pass')
    plt.show()
if __name__ == '__main__':
    print("ok")
    # data:
    X = np.array([[0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25, 2.50,2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75, 5.00, 5.50]])
    y = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1])

    #x = []
    #y1 = []
    #with open('logictis.csv', 'r') as file:
    #    reader = csv.reader(file)
    #    for row in reader:  # row là một ma trận có hai cột x,y
    #        x.append(row[0])  # thêm row[0](x) và mảng x
    #        y1.append(row[1])
    #        print(y1)
    #    X = np.array([x], dtype=float)
    #    y = np.array([y1], dtype=float)

    # extended data
    Xbar = np.concatenate((np.ones((1, X.shape[1])), X), axis=0) #ver
    eta = .07
    d = Xbar.shape[0]
    w_init = np.random.randn(d, 1)
    w = my_logistic_sigmoid_regression(Xbar, y, w_init, eta)
    print(w[-1].T)
    print(sigmoid(np.dot(w[-1].T,Xbar)))
    display(w,Xbar,y)

