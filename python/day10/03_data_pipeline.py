def load_data():
    return [80, 95, 70, 100, 85]


def analyze_data(scores):
    average = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)

    return average, highest, lowest


def display_result(average, highest, lowest):
    print(f"Average: {average}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")


def main():
    scores = load_data()

    average, highest, lowest = analyze_data(scores)

    display_result(average, highest, lowest)


if __name__ == "__main__":
    main()