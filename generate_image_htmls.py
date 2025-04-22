import mysql.connector
import os

def generate_html_from_database(output_folder="GeneratedHTMLs"):
    # Connect to the database
    connection = mysql.connector.connect(
        host='localhost',
        user=input("Enter the username: "),
        password=input("Enter your password: "),
        database=input("Enter the target database: ")
    )
    cursor = connection.cursor()

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
    cursor.close()
    connection.close()

# Call it!
generate_html_from_database()
