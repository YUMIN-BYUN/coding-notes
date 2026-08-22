import numpy as np
from scipy.optimize import curve_fit, minimize_scalar
from .models import exponential_model, sinusoidal_model, gaussian_model

def fit_linear(x, y, yerr=None):
    if yerr is None:
        coefficients, pcov = np.polyfit(x, y, 1, cov=True)
    else: 
        coefficients, pcov = np.polyfit(x, y, 1, w=1/yerr, cov="unscaled")
    a_1, a_0 = coefficients
    return a_1, a_0, pcov

def fit_polynomial(x, y, degree, yerr=None):
    if yerr is None:
        coefficients, pcov = np.polyfit(x, y, degree, cov=True)
    else:
        coefficients, pcov = np.polyfit(x, y, degree, w=1/yerr, cov="unscaled")
    return coefficients, pcov

def fit_exponential(x, y, initial_guess, yerr=None):
    if yerr is None:
        popt, pcov = curve_fit(
            exponential_model,
            x,
            y,
            p0 = initial_guess
        )
    else: 
        popt, pcov = curve_fit(
            exponential_model,
            x,
            y,
            p0=initial_guess,
            sigma=yerr,
            absolute_sigma=True
        )
    return popt, pcov

def exponential_guess_error(C0, x, y):
    shifted_y = y - C0
    log_y = np.log(np.abs(shifted_y))
    B0, log_A0 = np.polyfit(x, log_y, 1)
    
    A0_magnitude = np.exp(log_A0)
    sign_A = np.sign(np.mean(shifted_y))
    A0 = sign_A * A0_magnitude

    y_pred = exponential_model(x, A0, B0, C0)

    rss = np.sum((y-y_pred) ** 2)
    return rss


def estimate_exponential_guess(x, y):
    y_min = np.min(y)
    y_max = np.max(y)
    y_range = y_max - y_min

    # A > 0 branch: C < y_min
    lower_bound = y_min - y_range
    lower_upper_bound = np.nextafter(y_min, -np.inf)

    lower_result = minimize_scalar(
        exponential_guess_error,
        args=(x, y),
        bounds=(lower_bound, lower_upper_bound),
        method="bounded"
    )

    lower_C0 = lower_result.x
    lower_rss = lower_result.fun

    # A < 0 branch: C > y_max
    upper_lower_bound = np.nextafter(y_max, np.inf)
    upper_bound = y_max + y_range

    upper_result = minimize_scalar(
        exponential_guess_error,
        args=(x, y),
        bounds=(upper_lower_bound, upper_bound),
        method="bounded"
    )

    upper_C0 = upper_result.x
    upper_rss = upper_result.fun

    # Select better branch
    if lower_rss <= upper_rss:
        C0 = lower_C0
    else:
        C0 = upper_C0

    # Reconstruct A0 and B0 using selected C0
    shifted_y = y - C0
    log_y = np.log(np.abs(shifted_y))

    B0, log_A0 = np.polyfit(x, log_y, 1)

    A0_magnitude = np.exp(log_A0)
    sign_A = np.sign(np.mean(shifted_y))
    A0 = sign_A * A0_magnitude

    return [A0, B0, C0]

def fit_sinusoidal(x, y, initial_guess, yerr=None):
    if yerr is None:
        popt, pcov = curve_fit(
            sinusoidal_model,
            x,
            y,
            p0 = initial_guess
        )
    else: 
        popt, pcov = curve_fit(
            sinusoidal_model,
            x,
            y,
            p0=initial_guess,
            sigma=yerr,
            absolute_sigma=True
        )
    return popt, pcov

def estimate_sinusoidal_guess(x, y):
    A0 = (np.max(y) - np.min(y)) / 2
    C0 = (np.max(y) + np.min(y)) / 2

    dx = np.diff(x)

    if not np.allclose(dx, dx[0]):
        raise ValueError(
            "Automatic sinusoidal initial guess requires uniformly spaced x data."
        )

    delta_x = dx[0]
    y_centered = y - C0
    fft_values = np.fft.rfft(y_centered)
    frequencies = np.fft.rfftfreq(
        len(y),
        d=delta_x
    )

    magnitudes = np.abs(fft_values)
    dominant_index = np.argmax(magnitudes[1:]) + 1
    f0 = frequencies[dominant_index]
    omega0 = 2 * np.pi * f0

    phase_fft = np.angle(fft_values[dominant_index])
    phi0 = (
        phase_fft
        + np.pi / 2
        - omega0 * x[0]
    )
    phi0 = (phi0 + np.pi) % (2 * np.pi) - np.pi

    return [A0, omega0, phi0, C0]

def fit_gaussian(x, y, initial_guess, yerr=None):
    if yerr is None:
        popt, pcov = curve_fit(
            gaussian_model,
            x,
            y,
            p0=initial_guess
        )
    else:
        popt, pcov = curve_fit(
            gaussian_model,
            x,
            y,
            p0=initial_guess,
            sigma=yerr,
            absolute_sigma=True
        )

    return popt, pcov

def estimate_gaussian_guess(x, y):
    edge_count = max(1, len(y) // 10)

    C0 = np.mean(
        np.concatenate([
            y[:edge_count],
            y[-edge_count:]
        ])
    )

    peak_index = np.argmax(y)

    mu0 = x[peak_index]
    A0 = y[peak_index] - C0

    # Estimate sigma using FWHM
    half_max = C0 + A0 / 2

    left_index = np.argmin(
        np.abs(y[:peak_index] - half_max)
    )

    right_index = peak_index + np.argmin(
        np.abs(y[peak_index:] - half_max)
    )

    fwhm = x[right_index] - x[left_index]

    sigma0 = fwhm / (2 * np.sqrt(2 * np.log(2)))

    return [A0, mu0, sigma0, C0]


def calculate_parameter_uncertainties(pcov):
    return np.sqrt(np.diag(pcov))

def create_custom_model(expression, parameter_names):
    def custom_model(x, *params):
        local_variables = {
            "x": x
        }

        for name, value in zip(parameter_names, params):
            local_variables[name] = value

        safe_namespace = {
            "np": np
        }

        return eval(
            expression,
            {"__builtins__": {}},
            {
                **safe_namespace,
                **local_variables
            }
        )

    return custom_model


def fit_custom(
    x,
    y,
    expression,
    parameter_names,
    initial_guess,
    yerr=None
):
    custom_model = create_custom_model(
        expression,
        parameter_names
    )

    if yerr is None:
        popt, pcov = curve_fit(
            custom_model,
            x,
            y,
            p0=initial_guess
        )

    else:
        popt, pcov = curve_fit(
            custom_model,
            x,
            y,
            p0=initial_guess,
            sigma=yerr,
            absolute_sigma=True
        )

    return popt, pcov, custom_model