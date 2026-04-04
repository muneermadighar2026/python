my_dictionary = {
    "name": "Alice",
    "age": 30,
    "major": "computer Science"
}
# Accessing key
for key in my_dictionary:
    print(f"key: {key}")
print("----------------------------------")
# Accessing keys and values
for key in my_dictionary:
    value = my_dictionary[key]
    print(f"key: {key}, value: {value}")
print("----------------------------------")   
# Accessing only values
for value in my_dictionary.values():
    print(f"Value: {value}")
print("----------------------------------")
# Accessing key-value pairs (items) - Most pythonic way
for key, value in my_dictionary.items():
    print(f"Key: {key} \t Value: {value}")