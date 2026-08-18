import numpy as np

def fit_linear(x, y):
    a_1, a_0 = np.polyfit(x, y, 1)
    return a_1, a_0

def fit_polynomial(x, y, degree):
    coefficients = np.polyfit(x,y,degree)
    return coefficients