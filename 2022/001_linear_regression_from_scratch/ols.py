import numpy as np

def compute_ols(X, y):
    tX_X = np.matmul(np.array(X).transpose(), np.array(X))
    tX_X_1 = np.linalg.inv(tX_X)
    tX_X_1_tX = np.matmul(tX_X_1, X.transpose())
    W_hat = np.matmul(tX_X_1_tX, y)
    return W_hat
