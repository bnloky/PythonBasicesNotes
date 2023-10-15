def divide(x, y):

    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero!")
    else:
        print(f"Result of division: {result}")  #if you want to call the variable within in the double quotes, we need mention the 'f' keyword in the begin
    finally:   
        print("This code is always executed, whether there was an exception or not.")# Example 1: Division by a non-zero number
divide(10, 2)# Example 2: Division by zero (Exception case)
divide(10, 0)