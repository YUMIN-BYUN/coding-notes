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

def calculate_chi_squared(y, y_pred, yerr):
    residuals = y-y_pred

    chi_squared = np.sum(
        (residuals / yerr) ** 2
    )

    return chi_squared

def calculate_reduced_chi_squared(
        chi_squared,
        n_points,
        n_parameters
):
    degrees_of_freedom = n_points - n_parameters

    if degrees_of_freedom <= 0:
        raise ValueError(
            "Degrees of freedom must be positive."
        )

    reduced_chi_squared = (
        chi_squared / degrees_of_freedom
    )

    return reduced_chi_squared