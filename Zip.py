import csv
import os
import zipfile

# Function to calculate the size of a file in bytes
def get_file_size(file_path):
    return os.path.getsize(file_path)

# Read CSV file and store paths in a list
file_paths = []
with open('file_paths.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        file_paths.extend(row)

# Create an empty list to store batches
batches = []
current_batch = []
total_size = 0

# Iterate over file paths and group them into batches
for file_path in file_paths:
    file_size = get_file_size(file_path)
    if total_size + file_size > 40 * 1024 * 1024:  # Convert 40MB to bytes
        batches.append(current_batch)
        current_batch = []
        total_size = 0

    current_batch.append(file_path)
    total_size += file_size

# Add the last batch to the list if not empty
if current_batch:
    batches.append(current_batch)

# Create a new ZIP file and add files from each batch
with zipfile.ZipFile('batch_files.zip', 'w', zipfile.ZIP_DEFLATED) as zip_file:
    for i, batch in enumerate(batches):
        for file_path in batch:
            zip_file.write(file_path)

        # Add the CSV file to each batch
        zip_file.write('file_paths.csv', f'file_paths_batch{i+1}.csv')
