import pandas as pd
import zipfile
import os

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('your_file.csv')

# Group the rows by parent ID
grouped = df.groupby('parent ID')

# Specify the directory to save the zip files
save_directory = '/path/to/save/directory/'

# Create a new DataFrame to store zipping status
zipping_status_df = pd.DataFrame(columns=['parent ID', 'Zipping Status'])

# Iterate over each group
for parent_id, group in grouped:
    # Create a zip file with the parent ID as the name in the specified directory
    zip_file_path = os.path.join(save_directory, f'{parent_id}.zip')
    try:
        with zipfile.ZipFile(zip_file_path, 'w') as zipf:
            # Iterate over the rows in the group
            for _, row in group.iterrows():
                file_path = row['PATHS']
                # Add the file to the zip file
                zipf.write(file_path)
        # If zipping is successful, record the status as 'success'
        zipping_status_df = zipping_status_df.append({'parent ID': parent_id, 'Zipping Status': 'success'}, ignore_index=True)
    except:
        # If zipping fails, record the status as 'failure'
        zipping_status_df = zipping_status_df.append({'parent ID': parent_id, 'Zipping Status': 'failure'}, ignore_index=True)

# Write the zipping status DataFrame to a CSV file
zipping_status_df.to_csv('zipping_status.csv', index=False)