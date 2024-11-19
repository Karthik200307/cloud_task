import mysql.connector

# Database Configuration
db_config = {
    'user': 'admin',
    'password': 'your_password',
    'host': 'mydb.xxxxxx.us-east-1.rds.amazonaws.com',
    'database': 'testdb'
}

# Connect to the database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Execute a query
query = "SELECT FirstName, LastName, Department, Salary FROM Employees;"
cursor.execute(query)

# Fetch and display results
print("Employees:")
for row in cursor.fetchall():
    print(row)

# Close the connection
cursor.close()
conn.close()