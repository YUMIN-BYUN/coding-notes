import numpy as np
from scipy.optimize import curve_fit, minimize_scalar
from .models import exponential_model, sinusoidal_model

def fit_linear(x, y):
    a_1, a_0 = np.polyfit(x, y, 1)
    return a_1, a_0

def fit_polynomial(x, y, degree):
    coefficients = np.polyfit(x,y,degree)
    return coefficients

def fit_exponential(x, y, initial_guess):
    popt, pcov = curve_fit(
        exponential_model,
        x,
        y,
        p0 = initial_guess
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

def fit_sinusoidal(x, y, initial_guess):
    popt, pcov = curve_fit(
        sinusoidal_model,
        x,
        y,
        p0 = initial_guess
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