import pandas as pd
import zipfile
import os
import multiprocessing

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('your_file.csv')

# Group the rows by parent ID
grouped = df.groupby('parent ID')

# Specify the directory to save the zip files
save_directory = '/path/to/save/directory/'

# Create a new DataFrame to store zipping status
zipping_status_df = pd.DataFrame(columns=['parent ID', 'Zipping Status'])

# Function to zip files for a group in parallel
def zip_files(group):
    parent_id, rows = group
    zip_file_path = os.path.join(save_directory, f'{parent_id}.zip')
    try:
        with zipfile.ZipFile(zip_file_path, 'w') as zipf:
            for _, row in rows.iterrows():
                file_path = row['PATHS']
                filename = os.path.basename(file_path)
                zipf.write(file_path, arcname=filename)
        zipping_status_df.loc[len(zipping_status_df)] = {'parent ID': parent_id, 'Zipping Status': 'success'}
    except:
        zipping_status_df.loc[len(zipping_status_df)] = {'parent ID': parent_id, 'Zipping Status': 'failure'}

# Create a multiprocessing pool
pool = multiprocessing.Pool()

# Map the zip_files function to the grouped DataFrame in parallel
results = pool.map(zip_files, grouped)

# Close the multiprocessing pool
pool.close()
pool.join()

# Write the zipping status DataFrame to a CSV file
zipping_status_df.to_csv('zipping_status.csv', index=False)

# Log the results to a file
log_file = open('zipping_log.txt', 'w')
for result in results:
    log_file.write(f"{result}\n")
log_file.close()