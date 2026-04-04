def outer_function():
    print("This is the outer function.")
    def inner_function():
        print("This is the inner function.")
    inner_function()
outer_function()
# Output:
# This is the outer function.
# This is the inner function.
def print_hello_and_add(x, y):
  print("hello")
  def add_num(a, b):
    c = a + b
    return c
  result_sum = add_num(x, y)
  print(result_sum)
print_hello_and_add(2, 3)
# Output:
# hello
# 5