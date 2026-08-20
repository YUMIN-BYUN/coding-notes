import numpy as np

from src.data_loader import load_experimental_data
from src.models import linear_model, polynomial_model, exponential_model, sinusoidal_model
from src.fitting import fit_linear, fit_polynomial, fit_exponential, fit_sinusoidal, estimate_exponential_guess, estimate_sinusoidal_guess
from src.plotting import plot_fit, plot_residuals, show_plots
from src.metrics import calculate_residuals, calculate_r_squared, calculate_rmse

PLOT_POINTS = 500

# 1. Load data
file_path = input("Enter CSV file path: ")

x, y, yerr =  load_experimental_data(file_path)

# 2. Select model
print("\nSelect model:")
print("1. Linear")
print("2. Polynomial")
print("3. Exponential")
print("4. Sinusoidal")

choice = int(input("Choice: "))

# 3. Create x values for smooth fitted curve
x_fit = np.linspace(x.min(), x.max(), PLOT_POINTS)

# 4. Fit
if choice == 1:
    a, b = fit_linear(x, y)
    y_fit = linear_model(x_fit, a, b)
    y_pred = linear_model(x, a, b)

    print("\n=== Linear Fit Result ===")
    print("Slope: ", a)
    print("Intercept: ", b)

elif choice == 2:
    degree = int(input("Enter the degree: "))
    coefficients = fit_polynomial(x, y, degree)
    y_fit = polynomial_model(x_fit, coefficients)
    y_pred = polynomial_model(x, coefficients)

    print("\n=== Polynomial Fit Result ===")
    print("Degree: ", degree)
    print("Coefficients: ", coefficients)

elif choice == 3:
    initial_guess = estimate_exponential_guess(x, y)
    print("Initial guess:", initial_guess)

    popt, pcov = fit_exponential(x, y, initial_guess)
    A, B, C= popt

    y_fit = exponential_model(x_fit, A, B, C)
    y_pred = exponential_model(x, A, B, C)

    print("\n=== Exponential Fit Result ===")
    print("A: ", A)
    print("B: ", B)
    print("C: ", C)

elif choice == 4:
    initial_guess = estimate_sinusoidal_guess(x, y)
    print("Initial guess:", initial_guess)
    
    popt, pcov = fit_sinusoidal(x, y, initial_guess)
    A, omega, phi, C = popt

    y_fit = sinusoidal_model(x_fit, A, omega, phi, C)
    y_pred = sinusoidal_model(x, A, omega, phi, C)

    print("\n=== Sinusoidal Fit Result ===")
    print("A: ", A)
    print("omega: ", omega)
    print("phi: ", phi)
    print("C: ", C)

else: 
    print("Invalid choice")
    exit()

residuals = calculate_residuals(y, y_pred)
rmse = calculate_rmse(y, y_pred)
r_squared = calculate_r_squared(y, y_pred)

print(f"RMSE: {rmse}")
print(f"R^2: {r_squared}")
# 5. Plot settings

x_label = input("Enter the label of x axis: ")
x_unit = input("Enter the unit of x axis (leave blank if none): ")
y_label = input("Enter the label of y axis: ")
y_unit = input("Enter the unit of y axis (leave blank if none): ")
title = input("Enter the title of plot: ")

# 6. Plot
plot_fit(
    x,
    y,
    x_fit,
    y_fit,
    x_label,
    x_unit,
    y_label,
    y_unit,
    title
)

# 7. Residual plot
plot_residuals(
    x,
    residuals,
    x_label,
    x_unit,
    y_unit
)

show_plots()