try:
# Code that may raise an exception
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
except ZeroDivisionError:
# Handle the case where num2 is zero
    print("Error: Division by zero!")
except ValueError:
# Handle the case where user input is not a valid integer
    print("Error: Invalid input! Please enter a valid number.")
else:
# Code to execute when no exceptions are raised
    print(f"The result of division is:",result)