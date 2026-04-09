f = open('data.txt', 'r')
for line in f:  # Files are iterable objects, like lists
        print(line.upper())  # .strip() removes \n
f.close()