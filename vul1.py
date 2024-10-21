import sqlite3

def get_user_info(username):
    # Connect to the database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Vulnerable query - directly concatenating user input
    query = f"SELECT * FROM users WHERE username = '{username}'"

    # Execute the query
    cursor.execute(query)

    # Fetch and return user information
    user_info = cursor.fetchone()

    # Close the connection
    conn.close()

    return user_info


# Example usage
username = input("Enter your username: ")
username = "3epk3qe3 2q"
user_info = get_user_info(username)
if user_info:
    print("User found:", user_info)
else:
    print("User not found")
