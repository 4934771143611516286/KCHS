import mysql.connector

# Connect to your MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user=input("Enter the username: "),
    password=input("Enter your password: "),
    database=input("Enter the target database: ")
)

cursor = connection.cursor()

# Define the DELETE query
delete_query = "DELETE FROM imageimporttable WHERE id = %s"
user_id = (input("Enter the target ID to be deleted: "),)  # Tuple with one element

# Execute the query
cursor.execute(delete_query, user_id)

# Commit the change to the database
connection.commit()

print(f"{cursor.rowcount} row(s) deleted.")

# Close the cursor and connection
cursor.close()
connection.close()