def execute_user_code(user_code):
    # This is vulnerable to arbitrary code execution
    print(f"testing {user_code}")
    exec(user_code)

# Example usage
user_input = input("Enter some Python code to execute: ")
execute_user_code(user_input)
