# try:
#     filename = input("Enter a filename: ")
#     with open(filename, "r") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("File not found")
# except exception as e:
#     print(f"An error occured: {e}")
# finally:
#     print(f"Attempted to read a file {filename}.")

def count_lines_in_file(filename):
 line_count = 0
 try:
    with open(filename, 'r') as file:
        for line in file:
            line_count += 1
    print(f"The file '{filename}' has {line_count} lines.")
 except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
 except Exception as e:
    print(f"An unexpected error occurred: {e}")
 finally:
    print(f"Attempted to read file '{filename}'.")
if __name__ == "__main__":
    file_to_read = input("Enter the filename to read: ")
    count_lines_in_file(file_to_read)