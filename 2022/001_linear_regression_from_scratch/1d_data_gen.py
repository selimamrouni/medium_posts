import numpy as np 

#parameters
N = 100; a = 0.5; b = -10; sigma = 10
#Noise
sigma = np.random.normal(0, sigma, N)
# X
X = np.arange(0, N)
# y
y = a * X + b + sigma
# Trick
X = np.stack([np.ones(len(X)), X], axis = 1)