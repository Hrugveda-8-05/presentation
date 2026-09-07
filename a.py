import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Simulating user input with SQL injection payload
username = "admin' --"
password = "anything"

# ❌ VULNERABLE - string formatting directly into query
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
cursor.execute(query, params)

result = cursor.fetchone()
if result:
    print("Login successful!")  # This will succeed despite wrong password
