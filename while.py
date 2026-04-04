# count = 1
# while True : 
#     print(f"count is : {count}")
#     count = count + 1
# print("Loop is finished")

# Ask user for number
import time
val = int(input("Enter a number: "))
# Use while loop to count down from that number to 1, printing each number.
while val >= 1:
    print(val)
    time.sleep(1)
    val = val - 1
# After the loop, print "Blast off!"
print("Blast off!")