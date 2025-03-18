import csv
#import CSV file
# copied from https://automatetheboringstuff.com/chapter14/
def process_csv(filename):
    exampleFile = open(filename, encoding="utf-8")
    exampleReader = csv.reader(exampleFile)
    exampleData = list(exampleReader)
    exampleFile.close()
    return exampleData

#replace filepaths with wherever you're storing these files.
testerFilepath="Desktop/MVHS/Tester.csv"
htmlFilepath=""Desktop/MVHS/KCHS Image Display.html"

MyDB=process_csv(testerFilepath)
#print(MyDB)

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
            print("New row added successfully!")

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
    newHTML=open(str("Desktop/MVHS/KCHS-images-"+picTitle+"-"+picID+".html"),'w',encoding='utf-8')
    newHTML.write(newtext)
    newHTML.close()
    print("done!")
#add_row_to_csv(testerFilepath)
createHTMLforPhoto(htmlFilepath,"Testing","03/18/25","This is a testing description.","https://www.knoxhistory.org/templates/rt_studius/custom/images/headers/81623446_2819543581605978_5690387876819238912_n.jpg","12345")

    
