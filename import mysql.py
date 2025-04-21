import mysql.connector
import os

connection = mysql.connector.connect(
    host='localhost',
    user=input("Enter the username: "),
    password=input("Enter your password: "),
    database=input("Enter the target database: ")
)
cursor = connection.cursor()

def AddRowToDatabase():
    numEntries = int(input("How many items do you want to add? "))
    table_name = "imageimporttable"

        # Get columns (excluding auto-increment ID if any)
    cursor.execute(f"SHOW COLUMNS FROM {table_name}")
    columns_info = cursor.fetchall()
    column_names = [col[0] for col in columns_info if col[5] != 'auto_increment']

    addedRows = int(input("How many new items are you adding? "))

    for _ in range(addedRows):
        row_data = []
        for col in column_names:
            value = input(f"Enter value for '{col}': ").strip()
            row_data.append(value)

        # Create parameterized insert query
        placeholders = ", ".join(["%s"] * len(row_data))
        column_list = ", ".join(column_names)
        sql = f"INSERT INTO {table_name} ({column_list}) VALUES ({placeholders})"

        cursor.execute(sql, row_data)
        connection.commit()
        print("New photo added to database successfully!")
###
#connection = mysql.connector.connect(
    #host='localhost',
   # user=input("Enter the username: "),
  #  password=input("Enter your password: "),
 #   database=input("Enter the target database: ")
#)
#cursor = connection.cursor

# Get number of entries in DB to ensure no redundant IDs

# DB Fields: ID, dateTaken, Title, Link, Description, dateAdded

AddRowToDatabase()
