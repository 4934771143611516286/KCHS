import csv
import os

csvFilepathDefault="C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/ImportTester.csv" # Replace default filepaths w/ more generic ones.
htmlFilepathDefault="Desktop/MVHS/KCHS Image Display.html"

csvFilepathToUse ="Placeholder - CSV filepath" # Filepaths used actually entered into functions
htmlFilepathToUse ="Placeholder - HTML filepath"

# This is the file path used for the file that stores the CSV and HTML filepaths
pathsFileFP = "Placeholder - TXT filepath"


#import CSV file
# copied from https://automatetheboringstuff.com/chapter14/
def process_csv(filename):
    exampleFile = open(filename, encoding="utf-8")
    exampleReader = csv.reader(exampleFile)
    exampleData = list(exampleReader)
    exampleFile.close()
    return exampleData

# Function to create the file that is used to store the file paths if it doesn't exist already. Need to add a func for clearing the the file to get new inputs.
def check_or_create_file(filename="filepaths.txt"):
    # Get the path to the user's Documents folder
    documents_path = os.path.join(os.path.expanduser("~"), "Documents")
    
    # Make sure the Documents folder exists (usually does)
    if not os.path.exists(documents_path):
        print("Documents folder not found.")
        return

    # Full path to the file
    file_path = os.path.join(documents_path, filename)
    
    # Check if the file exists
    if os.path.isfile(file_path):
        print(f"File paths storage file exists: {file_path}")
    else:
        # Create the file
        with open(file_path, 'w') as f:
            f.write("")  # Write an empty string or default content
        print(f"File paths storage file created at: {file_path}")
    return file_path

# Function to get the file paths from the file, if not present
def get_filepaths(file_path):
    global csvFilepathToUse
    global htmlFilepathToUse
    # Ensure the file exists (create if not)
    if not os.path.exists(file_path):
        print("ERROR /// FILE PATHS STORAGE FILE DOES NOT EXIST")
        return

    # Read the first two lines
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Trim newline characters
    lines = [line.strip() for line in lines]

    # Initialize variables with default empty values
    csvPath = lines[0] if len(lines) > 0 else None
    htmlPath = lines[1] if len(lines) > 1 else None

    # Collect missing lines from user
    if not csvPath:
        csvPath = input("Input CSV path is missing: ")
    if not htmlPath:
        htmlPath = input("Output file path is missing: ")

    # Update file if any lines were missing
    if len(lines) < 2:
        with open(file_path, 'w') as f:
            f.write(csvPath + '\n')
            f.write(htmlPath + '\n')
    csvFilepathToUse = csvPath
    htmlFilepathToUse = htmlPath
    return



# Function to update the file paths from the file.
def update_filepaths(file_path):
    global csvFilepathToUse
    global htmlFilepathToUse
    # Ensure the file exists (create if not)
    if not os.path.exists(file_path):
        print("ERROR /// FILE PATHS STORAGE FILE DOES NOT EXIST")
        return


    # Glorp everything
    with open(file_path, 'w') as f:
        pass

    # Collect missing lines from user
    csvPath = input("Enter a new file path for the input: ")
    htmlPath = input("Enter a new file path for the output: ")

    # Update file if any lines were missing
    with open(file_path, 'w') as f:
        f.write(csvPath + '\n')
        f.write(htmlPath + '\n')
    csvFilepathToUse = csvPath
    htmlFilepathToUse = htmlPath
    return




def see_if_new_paths_are_desired(storageFilePath):
    global csvFilepathToUse
    global htmlFilepathToUse
    print("Would you like to use stored file paths or default file paths? \n")
    intention = input("Type \"D\" if you would like to use defaults. Type \"S\" if you would like to use stored file paths. Type \"N\" if you would like to enter new paths: \n")

    if intention == "D":
        csvFilepathToUse = csvFilepathDefault
        htmlFilepathToUse = htmlFilepathDefault
        return
    if intention == "S":
        get_filepaths(pathsFileFP)
        return
    if intention == "N":
        update_filepaths(pathsFileFP)
        return

pathsFileFP = check_or_create_file("filepaths.txt")
see_if_new_paths_are_desired(pathsFileFP)

MyDB=process_csv(csvFilepathToUse) #Change this to use filepaths from script
print(MyDB)

def dbCategories(file_path):
    try:
        with open(file_path, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            # Read the first row (or list) from the CSV file and return it
            categories = next(csv_reader)
            return categories
    except FileNotFoundError:
        print(f"File at {file_path} not found.")
    except Exception as e:
        print(f"Error: {e}")
        return []


# Function to add a new row to the CSV file
def add_row_to_csv(file_path):
    columns=dbCategories(file_path)
    # Open the CSV file in append mode
    addedRows=int(input("How many new items are you adding?"))
    for i in range(addedRows):
        with open(file_path, mode='a', newline='') as file:
            csv_writer = csv.writer(file)
            row=[]
            for j in columns:
                entry = input(f"Enter your image's {j}: ")
                # Convert the input string into a list by splitting by commas
                row.append(entry.strip())
            print(row)
            # Write the new row to the CSV file
            csv_writer.writerow(row)
            print("New photo added successfully!")

# Function to remove a row from CSV file based on ID
def remove_row_from_csv(input_file):
    removedID=input("Input the photo IDs you want to remove, separating each with a comma:  ")
    #creates list of IDs
    removedID.split(",")
    rows_to_keep = []
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.reader(infile)
        for row in reader:
            # Check if this row matches the ID and should be removed
            if row[0] not in removedID:
                rows_to_keep.append(row)
    # Rewrite CSV file with the filtered rows
    with open(input_file, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows_to_keep)
    print("Photos removed successfully!")

#function to create html site to display photo and information
def createHTMLforPhoto(HTMLbase,picTitle,picDate,picDesc,picImgLink,picID):
    oldHTML= open(HTMLbase, 'r', encoding='utf-8')
    newtext = oldHTML.read()
    newtext=newtext.replace("[Photo Title]",picTitle)
    newtext=newtext.replace("[Date Captured]",picDate)
    newtext=newtext.replace("[Description]", picDesc)
    newtext=newtext.replace("[Link]",picImgLink)
    newtext=newtext.replace("[Image Title + ID]",str(picTitle+picID))
    oldHTML.close()
    newHTML=open(str("KCHS-images-"+picTitle+"-"+picID+".html"),'w',encoding='utf-8')
    newHTML.write(newtext)
    newHTML.close()
    print("done!")


testing=input("\n \n Input 1 to add a row to the csv, 2 to remove, and 3 to create an html.  ")
if testing=="1":
    add_row_to_csv(csvFilepathToUse) # Replace w/ ToUse filepath vars rather than defaults porque func no work yet :(
elif testing=="2":
    remove_row_from_csv(csvFilepathToUse)
elif testing=="3":
    createHTMLforPhoto(htmlFilepathToUse,"Testing","03/18/25","This is a testing description.","https://www.knoxhistory.org/templates/rt_studius/custom/images/headers/81623446_2819543581605978_5690387876819238912_n.jpg","12345")
else:
    print("No effect, try again.")
    testing=input("\n \n Input 1 to add a row to the csv, 2 to remove, and 3 to create an html.  ")
