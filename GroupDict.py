import os
import csv

folder_path = '/path/to/folder'  # Replace with the actual folder path

table_names = set()  # To store unique table names
table_values = {}    # To store corresponding values for each table name

# Iterate through each CSV file in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)
        
        # Read the CSV file
        with open(file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                table_name = row['tablename']
                value = row['corresponding_value']
                
                # Add table name to the set of unique table names
                if value is not None and value != '':
                    table_names.add(table_name)
                    
                    # Store corresponding value for the table name
                    if table_name not in table_values:
                        table_values[table_name] = value

# Print the unique table names and their corresponding values
for table_name in table_names:
    value = table_values[table_name]
    print(f"Table name: {table_name}, Corresponding value: {value}")