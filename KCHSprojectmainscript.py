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
    table_name = "imageimporttable"

    # Get columns (excluding auto-increment ID if any)
    cursor.execute(f"SHOW COLUMNS FROM {table_name}")
    columns_info = cursor.fetchall()
    column_names = [col[0] for col in columns_info if col[5] != 'auto_increment']

    addedRows = int(input("How many new items are you adding? "))

    for rowNum in range(addedRows):
        row_data = []

        for col in column_names:
            # If the column is the ID, check for duplicates
            if col.lower() == "id":
                while True:
                    id_value = input(f"Enter value for '{col}': ").strip()
                    cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE id = %s", (id_value,))
                    (count,) = cursor.fetchone()
                    if count > 0:
                        print(f"An entry with ID '{id_value}' already exists. Please enter a unique ID.")
                    else:
                        row_data.append(id_value)
                        break
            else:
                value = input(f"Enter value for '{col}': ").strip()
                row_data.append(value)

        # Create parameterized insert query
        placeholders = ", ".join(["%s"] * len(row_data))
        column_list = ", ".join(column_names)
        sql = f"INSERT INTO {table_name} ({column_list}) VALUES ({placeholders})"

        cursor.execute(sql, row_data)
        connection.commit()
        print("New photo added to database successfully!")

    ChooseAction()

def RemoveRowFromDatabase():
    # Define the DELETE query
    select_query = "SELECT * FROM imageimporttable WHERE id = %s"
    delete_query = "DELETE FROM imageimporttable WHERE id = %s"
    
    numdeletions=int(input("How many entries would you like to delete? "))

    checksizequery = f"SELECT COUNT(*) FROM imageimporttable"
    cursor.execute(checksizequery)

    (row_count,) = cursor.fetchone()
    if numdeletions>row_count:
        print("Number of deleted entries is greater than the number of entries in the database!")
        RemoveRowFromDatabase()
    else:
        target = 1
        while target <= numdeletions:
            user_id = (input("Enter the target ID to be deleted: "),)  # Tuple with one element
            # Check if the ID exists
            cursor.execute(select_query, user_id)
            result = cursor.fetchone()

            if result:
                # ID exists, proceed to delete
                cursor.execute(delete_query, user_id)
                connection.commit()
                print(f"{cursor.rowcount} row(s) deleted.")
            else:
                print("No entry found with that ID. Nothing was deleted.")
                target -= 1
            target+=1

    # Close the cursor and connection
    #cursor.close()
    #connection.close()
    ChooseAction()

def generate_html_from_database(output_folder="GeneratedHTMLs"):
    global connection
    global cursor

    # Query all records
    cursor.execute("SELECT ID, dateTaken, Title, Link, Descript FROM imageimporttable")
    records = cursor.fetchall()

    # Load the HTML template
    with open("Desktop/MVHS/KCHS Image Display.html", 'r', encoding='utf-8') as template_file:
        template = template_file.read()

    # Make sure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for record in records:
        ID, dateTaken, Title, Link, Descript = record
        page_content = template.replace("[Photo Title]", Title)
        page_content = page_content.replace("[Date Captured]", str(dateTaken))
        page_content = page_content.replace("[Description]", Descript)
        page_content = page_content.replace("[Link]", Link)
        page_content = page_content.replace("[Image Title + ID]", f"{Title}_{ID}")

        output_filename = f"KCHS-image-{Title}-{ID}.html"
        output_path = os.path.join(output_folder, output_filename)

        with open(output_path, 'w', encoding='utf-8') as out_file:
            out_file.write(page_content)

        print(f"Generated: {output_filename}")
    # Clean up
    #cursor.close()
    #connection.close()
    ChooseAction()

def ChooseAction():
    choice = int(input("Would you like to add or remove entries from the database or create HTML files? Type \"1\" for entry, type \"2\" for removal, or type \"3\" for HTML creatiom.\n"))
    if choice == 1:
        AddRowToDatabase()
    elif choice == 2:
        RemoveRowFromDatabase()
    elif choice == 3:
        generate_html_from_database()
    else:
        print("Invalid input!")
        ChooseAction()
table = "imageimporttable"
query = f"SELECT COUNT(*) FROM imageimporttable"
cursor.execute(query)
(row_count,) = cursor.fetchone()

ChooseAction()
