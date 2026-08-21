import numpy as np

def linear_model(x, a, b):
    y_fit = a * x + b
    return y_fit

def polynomial_model(x, coefficients):
    y_fit = np.polyval(coefficients,x)
    return y_fit

def exponential_model(x, A, B, C):
    return A * np.exp(B * x) + C

def sinusoidal_model(x, A, omega, phi, C):
    return A * np.sin(omega * x + phi) + C

def gaussian_model(x, A, mu, sigma, C):
    return A * np.exp(-((x-mu)**2)/(2*sigma ** 2)) + C