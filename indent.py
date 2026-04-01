name = "Alice"
age = 30
if age >= 18:
    print(f"{name} is an adult.")  # indented — part of the if block
    print("They can vote.")        # also indented — part of the if block
else:
    print(f"{name} is a minor.")  # indented — part of the else block
print("This line is outside the if/else block.") # back to main level