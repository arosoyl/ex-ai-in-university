import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# hàm tính tanh sẽ chô độ chính xác cao hơn
def tanhFunc(x):
    return  (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))


# hàm tính loss: Loss = 1/m * (y*log(sigmoid) + (1-y)*log(1-sigmoid))
def compute_cost(X, y, w):
    m = len(y)
    z = tanhFunc(np.dot(X, w))
    J = np.sum(y * np.log(z) + (1 - y) * np.log(1 - z)) / m
    return J


def grad(X, y, w, alpha, loop):
    m = len(y)
    for i in range(loop):
        w = w - alpha * np.dot(X.T, tanhFunc(np.dot(X, w)) - y) / m
        # print(compute_cost(X, y, w))
        mix_id = np.random.permutation(m)
        X = X[mix_id]
        y = y[mix_id]
    return w


if __name__ == '__main__':
    df = pd.read_csv('logisticData.csv') # đọc file dữ liệu


    m, n = df.values.shape # m, n lần lượt là số hàng và cột
    # Tạo tập train
    X_train = df.values[:m-1, 0:n-1]  # tập input train là m-1 phần tử đầu (trừ cột cuối là là nhãn (output)
    y_train = df.values[:m-1, n-1:n]  # tương tự cho tập output train (lấy cột cuối)
    X_train = np.insert(X_train, 0, values=1, axis=1)
    # Tạo tập test
    # Tập test là dữ liệu của 1 hàng còn lại trong file dữ liệu
    X_test = df.values[m-1:, 0:n-1]
    X_test = np.insert(X_test, 0, values=1, axis=1)

    # threshold
    # giá trị xác định pred
    threshold = 0.5

    w = np.random.randn(n, 1)
    loop = 1000
    alpha = 0.002

    w = grad(X_train, y_train, w, alpha, loop)

    print('Final weights: \n', w)

    print('Evaluate:')

    pred_v = tanhFunc(np.dot(X_test[0], w))
    if (pred_v > threshold):
        pred_v = 1
    else:
        pred_v = 0
    #print(X_test)
    #print(X_train)
    #print(y_train)
    print('Predict:','A:',X_test[0][1],'B :',X_test[0][2], ' ----> result: ',pred_v)