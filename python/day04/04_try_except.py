try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Please enter an integer.")

except ZeroDivisionError:
    print("Zero is not allowed.")

except Exception as e:
    print("Unexpected error:", e)

else:
    print("Result:", result)

finally:
    print("Program finished.")