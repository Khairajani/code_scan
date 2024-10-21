def read_user_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
        return data

# Example usage
user_input = input("Enter the filename to read: ")
file_content = read_user_file(user_input)
print(file_content)
