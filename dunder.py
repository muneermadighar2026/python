# my_helper_functions.py
print(f"This line will always print when my_helper_functions.py is loaded. __name__ is: {__name__}")

def greet(name):
 return f"Hello, {name} from my_helper_functions!"

def add(a, b):
 return a + b

# This block only runs if my_helper_functions.py is executed directly
if __name__ == "__main__":
 print("my_helper_functions.py is being run directly!")
 user_name = input("Enter your name: ")
 print(greet(user_name))
 result = add(10, 5)
 print(f"The sum of 10 and 5 is: {result}")
 print("This is example usage or test code.")