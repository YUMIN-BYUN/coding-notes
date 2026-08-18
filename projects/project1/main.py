import numpy as np

from src.data_loader import load_experimental_data
from src.models import linear_model, polynomial_model 
from src.fitting import fit_linear, fit_polynomial
from src.plotting import plot_fit

PLOT_POINTS = 500

# 1. Load data
file_path = input("Enter CSV file path: ")

x, y, yerr =  load_experimental_data(file_path)

# 2. Select model
print("\nSelect model:")
print("1. Linear")
print("2. Polynomial")

choice = int(input("Choice: "))

# 3. Create x values for smooth fitted curve
x_fit = np.linspace(x.min(), x.max(), PLOT_POINTS)

# 4. Fit
if choice == 1:
    a, b = fit_linear(x, y)
    y_fit = linear_model(x_fit, a, b)

    print("\n=== Linear Fit Result ===")
    print("Slope: ", a)
    print("Intercept: ", b)

elif choice == 2:
    degree = int(input("Enter the degree: "))
    coefficients = fit_polynomial(x, y, degree)
    y_fit = polynomial_model(x_fit, coefficients)

    print("\n=== Polynomial Fit Result ===")
    print("Degree: ", degree)
    print("Coefficients: ", coefficients)

else: 
    print("Invalid choice")
    exit()

# 5. Plot settings
x_label = input("Enter the label of x axis: ")
y_label = input("Enter the label of y axis: ")
title = input("Enter the title of plot: ")


# 6. Plot
plot_fit(
    x,
    y,
    x_fit,
    y_fit,
    x_label,
    y_label,
    title
)