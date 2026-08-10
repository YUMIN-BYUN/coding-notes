def get_scores():
    text = input("Enter numbers separated by spaces: ")
    return [int(x) for x in text.split()]

def analyze_scores(scores):
    average = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)

    return average, highest, lowest

def display_result(average, highest, lowest):
    print(f"Average: {average}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")

def main():
    try:
        scores = get_scores()
        average, highest, lowest = analyze_scores(scores)
        display_result(average, highest, lowest)

    except ValueError:
        print("Please enter numbers only.")

    except ZeroDivisionError:
        print("No scores were entered.")

if __name__ == "__main__":
    main()

