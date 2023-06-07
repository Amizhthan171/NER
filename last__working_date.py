import os
import csv

folder_path = '/path/to/folder'  # Replace with the actual folder path
specific_table_name = 'YourSpecificTableName'  # Replace with the table name you want to search for

matching_files = []  # To store the names of CSV files containing the specific table name

# Iterate through each CSV file in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)
        
        # Read the CSV file
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as csv_file:
            reader = csv.DictReader(csv_file)
            
            # Check each row for the specific table name
            for row in reader:
                table_name = row['table name']
                
                if table_name == specific_table_name:
                    matching_files.append(file_name)
                    break  # Exit the loop since the table name is found in this file

# Print the names of CSV files containing the specific table name
if matching_files:
    print(f"The table name '{specific_table_name}' is present in the following CSV file(s):")
    for file_name in matching_files:
        print(file_name)
else:
    print(f"The table name '{specific_table_name}' is not found in any of the CSV files.")