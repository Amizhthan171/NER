import os
import csv

folder_path = '/path/to/folder'  # Replace with the actual folder path
key_to_find = 'keyA'

found = False  # Flag to indicate if the key is found

# Iterate through each CSV file in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)
        
        # Read the CSV file
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                key_value = row['key_column']
                unique_number = row['uniquenumber']
                
                # Check if the key matches
                if key_value == key_to_find:
                    found = True
                    
                    # Check if there is a corresponding value in the 'uniquenumber' column
                    if unique_number:
                        print(f"Found corresponding value '{unique_number}' for key '{key_to_find}' in file '{file_name}'")
                    else:
                        print(f"No corresponding value found for key '{key_to_find}' in file '{file_name}'")

# If the key is not found in any of the CSV files
if not found:
    print(f"Key '{key_to_find}' not found in any of the CSV files.")