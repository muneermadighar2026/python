try:
    while True:
        user_input = int(input("Enter an integer: "))
        print(user_input)
        break
except ValueError:
    print("Invalid input. Please enter a valid integer.")