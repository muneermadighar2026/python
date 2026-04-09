try:
    a = 10
    b = input("Enter a number to divide by: ")
    b = int(b)  # Can raise ValueError
    c = a / b       # Can raise ZeroDivisionError
    print(f"Result: {c}")
except ZeroDivisionError:
    print("Can not divide by zero")
except ValueError:
    print("Invalid input. Please enter a valid number")
except Exception as e:
    print(f"An error occured: {e} \n , please contact a developer")