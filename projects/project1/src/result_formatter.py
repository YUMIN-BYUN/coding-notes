def format_quick_result(result):
    lines = []

    lines.append(
        f"=== {result['model'].capitalize()} Fit ==="
    )

    lines.append("")

    for name, value, uncertainty in zip(
        result["parameter_names"],
        result["parameters"],
        result["parameter_uncertainties"]
    ):
        lines.append(
            f"{name} = {value:.6g} ± {uncertainty:.6g}"
        )

    lines.append("")

    lines.append(
        f"RMSE = {result['rmse']:.6g}"
    )

    if result["r_squared"] is None:
        lines.append(
            "R² = N/A"
        )
    else:
        lines.append(
            f"R² = {result['r_squared']:.6g}"
        )

    if result.get("reduced_chi_squared") is not None:
        lines.append(
            "Reduced χ² = "
            f"{result['reduced_chi_squared']:.6g}"
        )

    return "\n".join(lines)


def format_detail_result(result):
    lines = []

    lines.append("=== Fit Details ===")
    lines.append("")

    lines.append(
        f"Model: {result['model'].capitalize()}"
    )

    lines.append(
        f"Method: {result['fit_method']}"
    )

    # Custom model only
    if result.get("custom_expression") is not None:
        lines.append(
            "Expression: "
            f"{result['custom_expression']}"
        )

    # Nonlinear models only
    if result.get("initial_guess") is not None:
        lines.append(
            "Initial Guess: "
            f"{result['initial_guess']}"
        )

    lines.append("")
    lines.append("Parameters:")

    for name, value, uncertainty in zip(
        result["parameter_names"],
        result["parameters"],
        result["parameter_uncertainties"]
    ):
        lines.append(
            f"  {name} = "
            f"{value:.8g} ± {uncertainty:.8g}"
        )

    lines.append("")
    lines.append("Metrics:")

    lines.append(
        f"  RMSE = {result['rmse']:.8g}"
    )

    if result["r_squared"] is None:
        lines.append(
            "  R² = N/A"
        )
    else:
        lines.append(
            f"  R² = {result['r_squared']:.8g}"
        )

    if result.get("chi_squared") is not None:
        lines.append(
            f"  χ² = {result['chi_squared']:.8g}"
        )

    if result.get("reduced_chi_squared") is not None:
        lines.append(
            "  Reduced χ² = "
            f"{result['reduced_chi_squared']:.8g}"
        )

    lines.append(
        "  Degrees of Freedom = "
        f"{result['degrees_of_freedom']}"
    )

    return "\n".join(lines)