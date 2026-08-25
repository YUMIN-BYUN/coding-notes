import numpy as np

from src.analysis import run_fit
from src.result_formatter import format_quick_result


def run_test(name, function):
    print(f"\n=== {name} ===")

    try:
        function()
        print("FAILED: No error was raised.")

    except ValueError as error:
        print("PASSED")
        print("Caught:", error)


# ---------------------------------------------------------
# 1. x / y length mismatch
# ---------------------------------------------------------

def test_length_mismatch():
    run_fit(
        x=[1, 2, 3],
        y=[1, 2],
        model="linear"
    )


# ---------------------------------------------------------
# 2. Invalid yerr
# ---------------------------------------------------------

def test_invalid_yerr():
    run_fit(
        x=[1, 2, 3, 4],
        y=[2, 4, 6, 8],
        yerr=[0.1, -0.2, 0.1, 0.1],
        model="linear"
    )


# ---------------------------------------------------------
# 3. NaN data
# ---------------------------------------------------------

def test_nan():
    run_fit(
        x=[1, 2, 3, 4],
        y=[2, np.nan, 6, 8],
        model="linear"
    )


# ---------------------------------------------------------
# 4. Invalid polynomial degree
# ---------------------------------------------------------

def test_invalid_degree():
    run_fit(
        x=[0, 1, 2, 3],
        y=[1, 2, 5, 10],
        model="polynomial",
        degree=0
    )


# ---------------------------------------------------------
# 5. Too few data points
# ---------------------------------------------------------

def test_too_few_points():
    run_fit(
        x=[0, 1, 2],
        y=[1, 2, 5],
        model="polynomial",
        degree=2
    )


# ---------------------------------------------------------
# Run error tests
# ---------------------------------------------------------

run_test(
    "Length Mismatch",
    test_length_mismatch
)

run_test(
    "Invalid yerr",
    test_invalid_yerr
)

run_test(
    "NaN Data",
    test_nan
)

run_test(
    "Invalid Polynomial Degree",
    test_invalid_degree
)

run_test(
    "Too Few Data Points",
    test_too_few_points
)


# ---------------------------------------------------------
# 6. Constant y / R²
# ---------------------------------------------------------

print("\n=== Constant y Test ===")

try:
    result = run_fit(
        x=np.array([0, 1, 2, 3, 4], dtype=float),
        y=np.array([5, 5, 5, 5, 5], dtype=float),
        model="linear"
    )

    print(format_quick_result(result))

    if result["r_squared"] is None:
        print("PASSED: R² correctly returned N/A.")
    else:
        print("FAILED: R² should be None.")

except Exception as error:
    print("FAILED:", error)