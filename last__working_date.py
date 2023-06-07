import os
import csv
import pandas as pd

folder_path = '/path/to/folder'  # Replace with the actual folder path

table_names = set()  # To store unique table names
table_values = {}    # To store corresponding values for each table name

# Iterate through each CSV file in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)
        
        # Read the CSV file
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as csv_file:
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

# Create a dataframe from the unique table names and corresponding values
data = {'Table Name': list(table_names), 'Corresponding Value': [table_values[table_name] for table_name in table_names]}
df = pd.DataFrame(data)

# Print the dataframe
print(df)