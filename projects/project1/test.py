import numpy as np

from src.analysis import run_fit

from src.result_formatter import (
    format_quick_result,
    format_detail_result
)


# =========================================================
# Linear Test
# =========================================================

print("\n=== Linear Analysis Test ===")

x_linear = np.array(
    [0, 1, 2, 3, 4, 5],
    dtype=float
)

y_linear = np.array([
    3.1,
    4.9,
    7.2,
    8.8,
    11.1,
    13.0
])

yerr_linear = np.full(
    len(x_linear),
    0.2
)

result_linear = run_fit(
    x=x_linear,
    y=y_linear,
    model="linear",
    yerr=yerr_linear
)

print(format_quick_result(result_linear))


# =========================================================
# Polynomial Test
# =========================================================

print("\n=== Polynomial Analysis Test ===")

x_poly = np.array(
    [-2, -1, 0, 1, 2, 3],
    dtype=float
)

y_poly = np.array([
    19.1,
    9.9,
    5.2,
    3.8,
    6.9,
    14.1
])

yerr_poly = np.full(
    len(x_poly),
    0.2
)

result_poly = run_fit(
    x=x_poly,
    y=y_poly,
    model="polynomial",
    degree=2,
    yerr=yerr_poly
)

print(format_quick_result(result_poly))


# =========================================================
# Exponential Test
# =========================================================

print("\n=== Exponential Analysis Test ===")

x_exp = np.linspace(
    0,
    4,
    20
)

y_exp = (
    2 * np.exp(0.5 * x_exp)
    + 1
)

y_exp = y_exp + np.array([
    0.02, -0.03, 0.01, 0.04, -0.02,
    0.01, -0.01, 0.03, -0.02, 0.02,
    -0.01, 0.01, 0.03, -0.02, 0.01,
    -0.03, 0.02, 0.01, -0.01, 0.02
])

yerr_exp = np.full(
    len(x_exp),
    0.05
)

result_exp = run_fit(
    x=x_exp,
    y=y_exp,
    model="exponential",
    yerr=yerr_exp
)

print(format_quick_result(result_exp))


# =========================================================
# Sinusoidal Test
# =========================================================

print("\n=== Sinusoidal Analysis Test ===")

x_sin = np.linspace(
    0,
    4 * np.pi,
    100
)

rng_sin = np.random.default_rng(42)

y_sin = (
    3 * np.sin(
        2 * x_sin + 0.5
    )
    + 1
)

y_sin = y_sin + rng_sin.normal(
    0,
    0.05,
    size=len(x_sin)
)

yerr_sin = np.full(
    len(x_sin),
    0.05
)

result_sin = run_fit(
    x=x_sin,
    y=y_sin,
    model="sinusoidal",
    yerr=yerr_sin
)

print(format_quick_result(result_sin))


# =========================================================
# Gaussian Test
# =========================================================

print("\n=== Gaussian Analysis Test ===")

x_gauss = np.linspace(
    -3,
    5,
    100
)

rng_gauss = np.random.default_rng(42)

y_gauss = (
    5 * np.exp(
        -((x_gauss - 1) ** 2)
        / (2 * 0.8 ** 2)
    )
    + 1
)

y_gauss = y_gauss + rng_gauss.normal(
    0,
    0.05,
    size=len(x_gauss)
)

yerr_gauss = np.full(
    len(x_gauss),
    0.05
)

result_gauss = run_fit(
    x=x_gauss,
    y=y_gauss,
    model="gaussian",
    yerr=yerr_gauss
)

print(format_quick_result(result_gauss))


# =========================================================
# Custom Test
# =========================================================

print("\n=== Custom Analysis Test ===")

x_custom = np.linspace(
    -3,
    3,
    20
)

rng_custom = np.random.default_rng(42)

y_custom = (
    2 * x_custom**2
    - 3 * x_custom
    + 5
)

y_custom = y_custom + rng_custom.normal(
    0,
    0.2,
    size=len(x_custom)
)

yerr_custom = np.full(
    len(x_custom),
    0.2
)

result_custom = run_fit(
    x=x_custom,
    y=y_custom,
    model="custom",
    yerr=yerr_custom,
    custom_expression="A * x**2 + B * x + C",
    custom_parameter_names=[
        "A",
        "B",
        "C"
    ],
    initial_guess=[
        1,
        -1,
        1
    ]
)

print(format_quick_result(result_custom))


# =========================================================
# Quick / Detail Mode Test
# =========================================================

print("\n")
print("=" * 60)
print("QUICK MODE TEST")
print("=" * 60)

print(
    format_quick_result(
        result_gauss
    )
)


print("\n")
print("=" * 60)
print("DETAIL MODE TEST")
print("=" * 60)

print(
    format_detail_result(
        result_gauss
    )
)