num1 = float(input('enter First value'))
num2 = float(input('enter Second value'))
operation = input('enter operation (+, -, *, /)')
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    print('invalid operation')
print("Result:", result)