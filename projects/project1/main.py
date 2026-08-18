from src.data_loader import load_experimental_data

x, y, yerr = load_experimental_data("data/test_nan.csv")

print()
print("Loaded data")
print(f"x: {x}")
print(f"y: {y}")
print(f"y uncertainty: {yerr}")