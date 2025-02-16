import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("train.csv")
data_test = pd.read_csv("test.csv")

print(data)
print(data_test)

data = np.array(data)
m,n = data.shape
#print(f"m: {m}, n: {n}")
np.random.shuffle(data)

data_dev = data[0:1000].T

Y_test = data_dev[0]
X_test = data_dev[1:n]

data_train = data[1000:m].T
Y_train = data_train[0]
X_train = data_train[1:n]
X_train = X_train / 255.
_,m_train = X_train.shape
#print(Y_train)


def init_params():
    #was using rand n, needs rand. Generates arrays of the shape given
    # with values between -.5 and .5
    W1 = np.random.rand(10, 784) - 0.5
    b1 = np.random.rand(10, 1) - 0.5
    W2 = np.random.rand(10, 10) - 0.5
    b2 = np.random.rand(10, 1) - 0.5
    return W1, b1, W2, b2

def ReLU(x):
    #return x if x > 0. Otherwise, return 0. often replaces Sigmoid or Tanh
    return np.maximum(0, x)

def softmax(Z):
    #return np.exp(x) / np.sum(np.exp(x))
    Z -= np.max(Z, axis=0)
    A = np.exp(Z) / np.sum(np.exp(Z), axis=0)
    return A

def forward_prop(W1, b1, W2, b2, X):
    Z1 = W1.dot(X) + b1
    A1 = ReLU(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = softmax(Z2)
    return Z1, A1, Z2, A2

def one_hot(Y):
    one_hot_Y = np.zeros((Y.size, Y.max() + 1))
    one_hot_Y[np.arange(Y.size), Y] = 1
    return one_hot_Y.T

#return the slope of the relu function. 0 If Z <=0. 1 Otherwise, thus boolean ret is clean
def deriv_ReLU(Z):
    return Z > 0

def back_prop(Z1, A1, Z2, A2, W2, Y, X, one_hot_Y):
    m = Y.size
    dZ2 = A2 - one_hot_Y
    dW2 = 1 / m * dZ2.dot(A1.T)
    db2 = 1 / m * np.sum(dZ2)
    dZ1 = W2.T.dot(dZ2) *  deriv_ReLU(Z1)
    dW1 = 1 / m * dZ1.dot(X.T)
    db1 = 1/m * np.sum(dZ1)
    return dW1, db1, dW2, db2

def update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha):
    W1 -= alpha * dW1
    b1 -= alpha * db1
    W2 -= alpha * dW2
    b2 -= alpha * db2
    return W1, b1, W2, b2

def get_predictions(A2):
    return np.argmax(A2, 0)

def get_accuracy(predictions, Y):
    #print(predictions, Y)
    return np.sum(predictions == Y) / Y.size

def gradient_descent(X, Y, iterations, alpha):
    W1, b1, W2, b2 = init_params()
    one_hot_Y = one_hot(Y)
    for i in range(iterations):
        Z1, A1, Z2, A2 = forward_prop(W1, b1, W2, b2, X)
        dW1, db1, dW2, db2 = back_prop(Z1, A1, Z2, A2, W2, Y, X, one_hot_Y)
        W1, b1, W2, b2 = update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha)
        if i % 50 == 0:
            #print(f"W1: {W1 == w1init}, b1: {b1 == b1init}, W2: {W2 == w2init}, b2: {b2 == b2init}")
            print(f"Iteration: {i}")
            print(f"Accuracy: {np.floor(get_accuracy(get_predictions(A2), Y)*1000) / 10}%")
    return W1, b1, W2, b2

W1, b1, W2, b2 = gradient_descent(X_train, Y_train, 500, 0.1)


data_test = data_test.T
print(data_test.T)
print(data_test[0])