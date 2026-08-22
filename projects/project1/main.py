import numpy as np

from src.data_loader import load_experimental_data
from src.models import (
    linear_model,
    polynomial_model,
    exponential_model,
    sinusoidal_model,
    gaussian_model
)
from src.fitting import (
    fit_linear,
    fit_polynomial,
    fit_exponential,
    fit_sinusoidal,
    estimate_exponential_guess,
    estimate_sinusoidal_guess,
    fit_gaussian,
    estimate_gaussian_guess,
    calculate_parameter_uncertainties,
    fit_custom
)
from src.plotting import (
    plot_raw_data,
    plot_fit,
    plot_residuals,
    show_plots
)
from src.metrics import (
    calculate_residuals,
    calculate_r_squared,
    calculate_rmse,
    calculate_chi_squared,
    calculate_reduced_chi_squared
)

PLOT_POINTS = 500


# 1. Load data
file_path = input("Enter CSV file path: ")

x, y, yerr = load_experimental_data(file_path)

# 2. Axis settings
x_label = input("Enter the label of x axis: ")
x_unit = input("Enter the unit of x axis (leave blank if none): ")
y_label = input("Enter the label of y axis: ")
y_unit = input("Enter the unit of y axis (leave blank if none): ")

# 3. Raw data preview
while True:
    x_scale = input("Enter x-axis scale (linear/log): ").strip().lower()
    y_scale = input("Enter y-axis scale (linear/log): ").strip().lower()

    try:
        plot_raw_data(
            x,
            y,
            x_label,
            x_unit,
            y_label,
            y_unit,
            yerr,
            x_scale,
            y_scale
        )
        break

    except ValueError as e:
        print(f"Error: {e}")
        print("Please try again.\n")

# 4. Select model
print("\nSelect model:")
print("1. Linear")
print("2. Polynomial")
print("3. Exponential")
print("4. Sinusoidal")
print("5. Gaussian")
print("6. Custom")

choice = int(input("Choice: "))

# 5. Create x values for smooth fitted curve
x_fit = np.linspace(x.min(), x.max(), PLOT_POINTS)

# 6. Fit
if choice == 1:
    n_parameters = 2
    a, b, pcov = fit_linear(x, y, yerr)

    a_err, b_err = calculate_parameter_uncertainties(pcov)

    y_fit = linear_model(x_fit, a, b)
    y_pred = linear_model(x, a, b)

    print("\n=== Linear Fit Result ===")
    print(f"Slope: {a} ± {a_err}")
    print(f"Intercept: {b} ± {b_err}")

elif choice == 2:
    degree = int(input("Enter the degree: "))
    n_parameters = degree + 1

    coefficients, pcov = fit_polynomial(x, y, degree, yerr)

    parameter_errors = calculate_parameter_uncertainties(pcov)

    y_fit = polynomial_model(x_fit, coefficients)
    y_pred = polynomial_model(x, coefficients)

    print("\n=== Polynomial Fit Result ===")
    print("Degree:", degree)

    for i, (coefficient, error) in enumerate(
        zip(coefficients, parameter_errors)
    ):
        print(f"Coefficient {i}: {coefficient} ± {error}")

elif choice == 3:
    initial_guess = estimate_exponential_guess(x, y)
    n_parameters = 3
    print("Initial guess:", initial_guess)

    popt, pcov = fit_exponential(
        x,
        y,
        initial_guess,
        yerr
    )

    A, B, C = popt

    A_err, B_err, C_err = calculate_parameter_uncertainties(pcov)

    y_fit = exponential_model(x_fit, A, B, C)
    y_pred = exponential_model(x, A, B, C)

    print("\n=== Exponential Fit Result ===")
    print(f"A: {A} ± {A_err}")
    print(f"B: {B} ± {B_err}")
    print(f"C: {C} ± {C_err}")

elif choice == 4:
    initial_guess = estimate_sinusoidal_guess(x, y)
    n_parameters = 4
    print("Initial guess:", initial_guess)

    popt, pcov = fit_sinusoidal(
        x,
        y,
        initial_guess,
        yerr
    )

    A, omega, phi, C = popt

    A_err, omega_err, phi_err, C_err = (
        calculate_parameter_uncertainties(pcov)
    )

    y_fit = sinusoidal_model(
        x_fit,
        A,
        omega,
        phi,
        C
    )

    y_pred = sinusoidal_model(
        x,
        A,
        omega,
        phi,
        C
    )

    print("\n=== Sinusoidal Fit Result ===")
    print(f"A: {A} ± {A_err}")
    print(f"Omega: {omega} ± {omega_err}")
    print(f"Phi: {phi} ± {phi_err}")
    print(f"C: {C} ± {C_err}")

elif choice == 5:
    initial_guess = estimate_gaussian_guess(x, y)
    n_parameters = 4
    print("Initial guess:", initial_guess)

    popt, pcov = fit_gaussian(
        x,
        y,
        initial_guess,
        yerr
    )

    A, mu, sigma, C = popt

    A_err, mu_err, sigma_err, C_err = (
        calculate_parameter_uncertainties(pcov)
    )

    y_fit = gaussian_model(
        x_fit,
        A,
        mu,
        sigma,
        C
    )

    y_pred = gaussian_model(
        x,
        A,
        mu,
        sigma,
        C
    )

    print("\n=== Gaussian Fit Result ===")
    print(f"A: {A} ± {A_err}")
    print(f"Mu: {mu} ± {mu_err}")
    print(f"Sigma: {sigma} ± {sigma_err}")
    print(f"C: {C} ± {C_err}")

elif choice == 6:
    expression = input(
        "Enter custom function expression: "
    ).strip()

    parameter_input = input(
        "Enter parameter names separated by commas: "
    ).strip()

    parameter_names = [
        name.strip()
        for name in parameter_input.split(",")
    ]

    initial_guess_input = input(
        "Enter initial guesses separated by commas: "
    ).strip()

    initial_guess = [
        float(value.strip())
        for value in initial_guess_input.split(",")
    ]

    if len(parameter_names) != len(initial_guess):
        raise ValueError(
            "The number of parameter names and initial guesses must match."
        )

    n_parameters = len(parameter_names)

    popt, pcov, custom_model = fit_custom(
        x,
        y,
        expression,
        parameter_names,
        initial_guess,
        yerr
    )

    parameter_errors = (
        calculate_parameter_uncertainties(pcov)
    )

    y_fit = custom_model(
        x_fit,
        *popt
    )

    y_pred = custom_model(
        x,
        *popt
    )

    print("\n=== Custom Function Fit Result ===")
    print("Expression:", expression)

    for name, value, error in zip(
        parameter_names,
        popt,
        parameter_errors
    ):
        print(
            f"{name}: {value} ± {error}"
        )

else:
    print("Invalid choice")
    exit()

# 7. Calculate metrics
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

if yerr is not None:
    chi_squared = calculate_chi_squared(
        y,
        y_pred,
        yerr
    )

    reduced_chi_squared = calculate_reduced_chi_squared(
        chi_squared,
        len(y),
        n_parameters
    )

    print(f"Chi-squared: {chi_squared}")
    print(
        f"Reduced chi-squared: "
        f"{reduced_chi_squared}"
    )

print(f"RMSE: {rmse}")
print(f"R^2: {r_squared}")

# 8. Plot title
title = input("Enter the title of plot: ")

# 9. Fit plot
plot_fit(
    x,
    y,
    x_fit,
    y_fit,
    x_label,
    x_unit,
    y_label,
    y_unit,
    title,
    yerr
)

# 10. Residual plot
plot_residuals(
    x,
    residuals,
    x_label,
    x_unit,
    y_unit
)

# 11. Show fit and residual plots
show_plots()