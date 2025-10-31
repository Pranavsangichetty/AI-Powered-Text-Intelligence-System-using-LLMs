import sqlite3

# Connect to (or create) the SQLite database
conn = sqlite3.connect("database.db")
cur = conn.cursor()

# Create the employees table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER NOT NULL
)
""")

# Insert sample employee data
dummy_data = [
    ("Yuvraj", "Engineering", 85000),
    ("Sriram Reddy", "Human Resources", 60000),
    ("Suraj Kumar", "Engineering", 95000),
    ("Hemanth Shiva", "Finance", 72000),
    ("Abhiram", "Marketing", 68000),
    ("Jale Venkat", "Engineering", 88000),
    ("Pranav Kumar", "IT", 79000),
    ("Vara Prasad", "Finance", 73000),
    ("Rajath Rao", "IT", 81000),
    ("Shiva Kumar", "Marketing", 66000)
]

# Clear previous data (optional, for reset)
cur.execute("DELETE FROM employees")

# Insert all dummy records
cur.executemany("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)", dummy_data)
conn.commit()

print("Dummy table 'employees' created and populated successfully!")

# Verify
for row in cur.execute("SELECT * FROM employees LIMIT 5"):
    print(row)

conn.close()
