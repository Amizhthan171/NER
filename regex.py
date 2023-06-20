import pandas as pd
import zipfile
import os

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('your_file.csv')

# Group the rows by parent ID
grouped = df.groupby('parent ID')

# Specify the directory to save the zip files
save_directory = '/path/to/save/directory/'

# Iterate over each group
for parent_id, group in grouped:
    # Create a zip file with the parent ID as the name in the specified directory
    zip_file_path = os.path.join(save_directory, f'{parent_id}.zip')
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        # Iterate over the rows in the group
        for _, row in group.iterrows():
            file_path = row['PATHS']
            # Add the file to the zip file
            zipf.write(file_path)