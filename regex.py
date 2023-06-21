import pandas as pd
import zipfile

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('your_file.csv')

# Group the rows by parent ID
grouped = df.groupby('parent ID')

# Create a new DataFrame to store zipping status
zipping_status_df = pd.DataFrame(columns=['parent ID', 'Zipping Status'])

# Iterate over each group
for parent_id, group in grouped:
    # Create a zip file with the parent ID as the name
    zip_file_name = f'{parent_id}.zip'
    try:
        with zipfile.ZipFile(zip_file_name, 'w') as zipf:
            # Iterate over the rows in the group
            for _, row in group.iterrows():
                file_path = row['PATHS']
                # Add the file to the zip file
                zipf.write(file_path)
        # If zipping is successful, record the status as 'pass'
        zipping_status_df = zipping_status_df.append({'parent ID': parent_id, 'Zipping Status': 'pass'}, ignore_index=True)
    except:
        # If zipping fails, record the status as 'fail'
        zipping_status_df = zipping_status_df.append({'parent ID': parent_id, 'Zipping Status': 'fail'}, ignore_index=True)

# Write the zipping status DataFrame to a CSV file
zipping_status_df.to_csv('zipping_status.csv', index=False)