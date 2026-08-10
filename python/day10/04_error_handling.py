def get_numbers():
    text = input("Enter numbers separated by spaces: ")
    return [int(x) for x in text.split()]


def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def main():
    try:
        numbers = get_numbers()
        average = calculate_average(numbers)

        print(f"Average: {average}")

    except ValueError:
        print("Please enter numbers only.")

    except ZeroDivisionError:
        print("No numbers were entered.")


if __name__ == "__main__":
    main()