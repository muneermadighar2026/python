# main_app.py
import dunder  # Importing the module

print(f"Running newcode.py. __name__ here is: {__name__}")
message = dunder.greet("Bob")
print(message)
sum_result = dunder.add(7, 3)
print(f"From newcode, the sum is: {sum_result}")