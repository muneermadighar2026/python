# Reading with 'with'
with open('data.txt', 'r') as f:
        content = f.read()
        print(content)
        
#Write with 'with'
with open('data.txt', 'w') as f:
        f.write("Hello from the 'with' statement.\n")
        f.write("This file will auto-close.\n")
print("Data written to data.txt")