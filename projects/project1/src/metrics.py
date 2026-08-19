import numpy as np

def calculate_residuals(y, y_pred):
    return y-y_pred

def calculate_rmse(y, y_pred):
    res = calculate_residuals(y, y_pred)
    rmse = np.sqrt(np.mean(res**2)) 
    return rmse

def calculate_r_squared(y, y_pred):
    ss_res = np.sum(calculate_residuals(y, y_pred)**2)
    ss_tot = np.sum((y-np.mean(y))**2)
    return 1 - ss_res / ss_tot