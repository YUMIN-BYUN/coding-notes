import csv
import json
import numpy as np


def _convert_to_serializable(value):
    if isinstance(value, np.ndarray):
        return value.tolist()

    if isinstance(value, np.generic):
        return value.item()

    return value


def save_result_json(result, file_path):
    serializable_result = {}

    for key, value in result.items():
        serializable_result[key] = _convert_to_serializable(value)

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            serializable_result,
            file,
            indent=4,
            ensure_ascii=False
        )


def save_result_csv(result, file_path):
    with open(
        file_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Item",
            "Value"
        ])

        writer.writerow([
            "Model",
            result["model"]
        ])

        writer.writerow([
            "Fit Method",
            result["fit_method"]
        ])

        if result["custom_expression"] is not None:
            writer.writerow([
                "Custom Expression",
                result["custom_expression"]
            ])

        if result["initial_guess"] is not None:
            writer.writerow([
                "Initial Guess",
                result["initial_guess"].tolist()
            ])

        writer.writerow([])

        writer.writerow([
            "Parameter",
            "Value",
            "Uncertainty"
        ])

        for name, value, uncertainty in zip(
            result["parameter_names"],
            result["parameters"],
            result["parameter_uncertainties"]
        ):
            writer.writerow([
                name,
                value,
                uncertainty
            ])

        writer.writerow([])

        writer.writerow([
            "RMSE",
            result["rmse"]
        ])

        writer.writerow([
            "R Squared",
            result["r_squared"]
        ])

        writer.writerow([
            "Chi Squared",
            result["chi_squared"]
        ])

        writer.writerow([
            "Reduced Chi Squared",
            result["reduced_chi_squared"]
        ])

        writer.writerow([
            "Degrees of Freedom",
            result["degrees_of_freedom"]
        ])


def save_figure(
    figure,
    file_path,
    dpi=300
):
    figure.savefig(
        file_path,
        dpi=dpi,
        bbox_inches="tight"
    )