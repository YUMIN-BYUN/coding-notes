import numpy as np

def linear_model(x, a, b):
    y_fit = a * x + b
    return y_fit

def polynomial_model(x, coefficients):
    y_fit = np.polyval(coefficients,x)
    return y_fit