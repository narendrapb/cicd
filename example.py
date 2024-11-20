import sqlite3

def vulnerable_function(user_input):
    # Hardcoded credentials (security vulnerability)
    db_password = "hardcoded_password"

    # SQL Injection vulnerability: unsafe usage of user input in SQL query
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor.execute(query)  # Unsafe: user_input is not sanitized
    result = cursor.fetchall()
    conn.close()
    return result

# Insecure deserialization vulnerability
import pickle

def insecure_deserialization(data):
    # Accepts untrusted serialized data, potentially leading to code execution
    obj = pickle.loads(data)
    return obj

# Example usage
if __name__ == "__main__":
    user_input = input("Enter username: ")
    print(vulnerable_function(user_input))

    malicious_data = b"cos\nsystem\n(S'rm -rf /'\ntR."
    insecure_deserialization(malicious_data)

