import csv
#import CSV file
# copied from https://automatetheboringstuff.com/chapter14/
def process_csv(filename):
    exampleFile = open(filename, encoding="utf-8")
    exampleReader = csv.reader(exampleFile)
    exampleData = list(exampleReader)
    exampleFile.close()
    return exampleData

filepath="Desktop/MVHS/Tester.csv"

MyDB=process_csv("Desktop/MVHS/Tester.csv")
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
            # Ask the user for input data
            row=[]
            for j in columns:
                entry = input(f"Enter your image's {j}: ")
                # Convert the input string into a list by splitting by commas
                row.append(entry.strip())
            print(row)
            # Write the new row to the CSV file
            csv_writer.writerow(row)
            print("New row added successfully!")


add_row_to_csv(filepath)