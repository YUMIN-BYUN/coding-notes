import numpy as np

from src.fitting import (
    fit_linear,
    fit_polynomial,
    fit_exponential,
    estimate_exponential_guess,
    fit_sinusoidal,
    estimate_sinusoidal_guess,
    fit_gaussian,
    estimate_gaussian_guess,
    fit_custom
)

from src.models import (
    linear_model,
    polynomial_model,
    exponential_model,
    sinusoidal_model,
    gaussian_model
)

from src.metrics import (
    calculate_residuals,
    calculate_rmse,
    calculate_r_squared,
    calculate_chi_squared,
    calculate_reduced_chi_squared,
)


def _build_fit_result(
    result,
    y,
    yerr,
    parameters,
    covariance,
    parameter_names,
    y_pred,
    fit_type,
):
    # Parameter uncertainty
    parameter_uncertainties = np.sqrt(
        np.diag(covariance)
    )

    # Residuals and basic metrics
    residuals = calculate_residuals(
        y,
        y_pred
    )

    rmse = calculate_rmse(
        y,
        y_pred
    )

    r_squared = calculate_r_squared(
        y,
        y_pred
    )

    # Degrees of freedom
    number_of_parameters = len(parameters)
    degrees_of_freedom = len(y) - number_of_parameters

    if degrees_of_freedom <= 0:
        raise ValueError(
            "The number of data points must be greater "
            "than the number of fitted parameters."
        )

    # Determine fitting method
    if yerr is None:
        fit_method = f"Ordinary {fit_type} Least Squares"
    else:
        fit_method = f"Weighted {fit_type} Least Squares"

    # Chi-squared metrics
    if yerr is not None:
        chi_squared = calculate_chi_squared(
            y,
            y_pred,
            yerr
        )

        reduced_chi_squared = calculate_reduced_chi_squared(
            chi_squared,
            len(y),
            number_of_parameters
        )

    else:
        chi_squared = None
        reduced_chi_squared = None

    # Store results
    result.update({
        "fit_method": fit_method,

        "parameter_names": parameter_names,
        "parameters": parameters,
        "parameter_uncertainties": parameter_uncertainties,

        "y_pred": y_pred,
        "residuals": residuals,

        "rmse": rmse,
        "r_squared": r_squared,

        "chi_squared": chi_squared,
        "reduced_chi_squared": reduced_chi_squared,
        "degrees_of_freedom": degrees_of_freedom,
    })

    return result


def run_fit(
    x,
    y,
    model,
    yerr=None,
    degree=None,
    initial_guess=None,
    custom_expression=None,
    custom_parameter_names=None,
):
    """
    Run one complete fitting workflow.
    """

    # -----------------------------------------------------
    # Convert input data to NumPy arrays
    # -----------------------------------------------------

    x = np.asarray(
        x,
        dtype=float
    )

    y = np.asarray(
        y,
        dtype=float
    )

    if yerr is not None:
        yerr = np.asarray(
            yerr,
            dtype=float
        )

    # -----------------------------------------------------
    # Common input validation
    # -----------------------------------------------------

    if x.ndim != 1 or y.ndim != 1:
        raise ValueError(
            "x and y must be one-dimensional arrays."
        )

    if len(x) != len(y):
        raise ValueError(
            "x and y must have the same length."
        )

    if len(x) == 0:
        raise ValueError(
            "Input data cannot be empty."
        )

    if not np.all(np.isfinite(x)):
        raise ValueError(
            "x contains NaN or infinite values."
        )

    if not np.all(np.isfinite(y)):
        raise ValueError(
            "y contains NaN or infinite values."
        )

    if yerr is not None:

        if yerr.ndim != 1:
            raise ValueError(
                "yerr must be a one-dimensional array."
            )

        if len(yerr) != len(y):
            raise ValueError(
                "yerr must have the same length as y."
            )

        if not np.all(np.isfinite(yerr)):
            raise ValueError(
                "yerr contains NaN or infinite values."
            )

        if np.any(yerr <= 0):
            raise ValueError(
                "All yerr values must be positive."
            )

    # -----------------------------------------------------
    # Normalize model name
    # -----------------------------------------------------

    model = model.lower()

    # -----------------------------------------------------
    # Common result structure
    # -----------------------------------------------------

    result = {
        "model": model,
        "fit_method": None,

        "parameter_names": None,
        "parameters": None,
        "parameter_uncertainties": None,

        "initial_guess": None,
        "custom_expression": None,

        "y_pred": None,
        "residuals": None,

        "rmse": None,
        "r_squared": None,

        "chi_squared": None,
        "reduced_chi_squared": None,
        "degrees_of_freedom": None,
    }

    # =====================================================
    # Linear
    # =====================================================

    if model == "linear":

        if len(x) <= 2:
            raise ValueError(
                "Linear fitting requires more than "
                "2 data points."
            )

        a, b, covariance = fit_linear(
            x,
            y,
            yerr=yerr
        )

        parameters = np.array([
            a,
            b
        ])

        parameter_names = [
            "a",
            "b"
        ]

        y_pred = linear_model(
            x,
            *parameters
        )

        return _build_fit_result(
            result=result,
            y=y,
            yerr=yerr,
            parameters=parameters,
            covariance=covariance,
            parameter_names=parameter_names,
            y_pred=y_pred,
            fit_type="Linear",
        )

    # =====================================================
    # Polynomial
    # =====================================================

    elif model == "polynomial":

        if degree is None:
            raise ValueError(
                "Polynomial degree is required."
            )

        if not isinstance(degree, int):
            raise ValueError(
                "Polynomial degree must be an integer."
            )

        if degree < 1:
            raise ValueError(
                "Polynomial degree must be at least 1."
            )

        number_of_parameters = degree + 1

        if len(x) <= number_of_parameters:
            raise ValueError(
                "The number of data points must be greater "
                "than the number of polynomial parameters."
            )

        coefficients, covariance = fit_polynomial(
            x,
            y,
            degree,
            yerr=yerr
        )

        parameters = np.array(
            coefficients
        )

        parameter_names = [
            f"a_{power}"
            for power in range(
                degree,
                -1,
                -1
            )
        ]

        y_pred = polynomial_model(
            x,
            parameters
        )

        return _build_fit_result(
            result=result,
            y=y,
            yerr=yerr,
            parameters=parameters,
            covariance=covariance,
            parameter_names=parameter_names,
            y_pred=y_pred,
            fit_type="Polynomial",
        )

    # =====================================================
    # Exponential
    # =====================================================

    elif model == "exponential":

        if len(x) <= 3:
            raise ValueError(
                "Exponential fitting requires more than "
                "3 data points."
            )

        if initial_guess is None:
            initial_guess = estimate_exponential_guess(
                x,
                y
            )

        if len(initial_guess) != 3:
            raise ValueError(
                "Exponential initial guess must contain "
                "3 values: A, B, C."
            )

        parameters, covariance = fit_exponential(
            x,
            y,
            initial_guess,
            yerr=yerr
        )

        parameters = np.asarray(
            parameters,
            dtype=float
        )

        parameter_names = [
            "A",
            "B",
            "C"
        ]

        y_pred = exponential_model(
            x,
            *parameters
        )

        result["initial_guess"] = np.asarray(
            initial_guess,
            dtype=float
        )

        return _build_fit_result(
            result=result,
            y=y,
            yerr=yerr,
            parameters=parameters,
            covariance=covariance,
            parameter_names=parameter_names,
            y_pred=y_pred,
            fit_type="Nonlinear",
        )

    # =====================================================
    # Sinusoidal
    # =====================================================

    elif model == "sinusoidal":

        if len(x) <= 4:
            raise ValueError(
                "Sinusoidal fitting requires more than "
                "4 data points."
            )

        if initial_guess is None:
            initial_guess = estimate_sinusoidal_guess(
                x,
                y
            )

        if len(initial_guess) != 4:
            raise ValueError(
                "Sinusoidal initial guess must contain "
                "4 values: A, omega, phi, C."
            )

        parameters, covariance = fit_sinusoidal(
            x,
            y,
            initial_guess,
            yerr=yerr
        )

        parameters = np.asarray(
            parameters,
            dtype=float
        )

        parameter_names = [
            "A",
            "omega",
            "phi",
            "C"
        ]

        y_pred = sinusoidal_model(
            x,
            *parameters
        )

        result["initial_guess"] = np.asarray(
            initial_guess,
            dtype=float
        )

        return _build_fit_result(
            result=result,
            y=y,
            yerr=yerr,
            parameters=parameters,
            covariance=covariance,
            parameter_names=parameter_names,
            y_pred=y_pred,
            fit_type="Nonlinear",
        )

    # =====================================================
    # Gaussian
    # =====================================================

    elif model == "gaussian":

        if len(x) <= 4:
            raise ValueError(
                "Gaussian fitting requires more than "
                "4 data points."
            )

        if initial_guess is None:
            initial_guess = estimate_gaussian_guess(
                x,
                y
            )

        if len(initial_guess) != 4:
            raise ValueError(
                "Gaussian initial guess must contain "
                "4 values: A, mu, sigma, C."
            )

        parameters, covariance = fit_gaussian(
            x,
            y,
            initial_guess,
            yerr=yerr
        )

        parameters = np.asarray(
            parameters,
            dtype=float
        )

        parameter_names = [
            "A",
            "mu",
            "sigma",
            "C"
        ]

        y_pred = gaussian_model(
            x,
            *parameters
        )

        result["initial_guess"] = np.asarray(
            initial_guess,
            dtype=float
        )

        return _build_fit_result(
            result=result,
            y=y,
            yerr=yerr,
            parameters=parameters,
            covariance=covariance,
            parameter_names=parameter_names,
            y_pred=y_pred,
            fit_type="Nonlinear",
        )

    # =====================================================
    # Custom
    # =====================================================

    elif model == "custom":

        if custom_expression is None:
            raise ValueError(
                "Custom expression is required."
            )

        if custom_expression.strip() == "":
            raise ValueError(
                "Custom expression cannot be empty."
            )

        if custom_parameter_names is None:
            raise ValueError(
                "Custom parameter names are required."
            )

        if len(custom_parameter_names) == 0:
            raise ValueError(
                "At least one custom parameter is required."
            )

        if initial_guess is None:
            raise ValueError(
                "Initial guess is required for custom fitting."
            )

        if len(custom_parameter_names) != len(initial_guess):
            raise ValueError(
                "The number of parameter names must match "
                "the number of initial guesses."
            )

        if len(x) <= len(custom_parameter_names):
            raise ValueError(
                "The number of data points must be greater "
                "than the number of custom parameters."
            )

        parameters, covariance, custom_model = fit_custom(
            x,
            y,
            custom_expression,
            custom_parameter_names,
            initial_guess,
            yerr=yerr
        )

        parameters = np.asarray(
            parameters,
            dtype=float
        )

        parameter_names = list(
            custom_parameter_names
        )

        y_pred = custom_model(
            x,
            *parameters
        )

        result["initial_guess"] = np.asarray(
            initial_guess,
            dtype=float
        )

        result["custom_expression"] = custom_expression

        return _build_fit_result(
            result=result,
            y=y,
            yerr=yerr,
            parameters=parameters,
            covariance=covariance,
            parameter_names=parameter_names,
            y_pred=y_pred,
            fit_type="Nonlinear",
        )

    # =====================================================
    # Invalid Model
    # =====================================================

    else:
        raise ValueError(
            f"Unsupported model: {model}"
        )