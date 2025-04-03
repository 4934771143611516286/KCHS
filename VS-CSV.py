import csv
#import CSV file
# copied from https://automatetheboringstuff.com/chapter14/
def process_csv(filename):
    exampleFile = open(filename, encoding="utf-8")
    exampleReader = csv.reader(exampleFile)
    exampleData = list(exampleReader)
    exampleFile.close()
    return exampleData

csvFilepath="Tester.csv"
htmlFilepath="KCHS Image Display.html"

MyDB=process_csv(csvFilepath)
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
    add_row_to_csv(csvFilepath)
elif testing=="2":
    remove_row_from_csv(csvFilepath)
elif testing=="3":
    createHTMLforPhoto(htmlFilepath,"Testing","03/18/25","This is a testing description.","https://www.knoxhistory.org/templates/rt_studius/custom/images/headers/81623446_2819543581605978_5690387876819238912_n.jpg","12345")
else:
    print("No effect, try again.")
    testing=input("\n \n Input 1 to add a row to the csv, 2 to remove, and 3 to create an html.  ")
