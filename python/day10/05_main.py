import data
import analysis


def main():
    try:
        scores = data.load_scores()

        average = analysis.calculate_average(scores)
        highest = analysis.find_highest(scores)
        lowest = analysis.find_lowest(scores)

        print(f"Average: {average}")
        print(f"Highest: {highest}")
        print(f"Lowest: {lowest}")

    except ZeroDivisionError:
        print("No data available.")


if __name__ == "__main__":
    main()