f = open('data.txt', 'r')
content = f.read()  # Reads the whole file into a string
print("--- Entire Content ---")
print(content)
f.close()  # Always close the file