import os
import shutil
from itertools import groupby

# Assuming you have a DataFrame named 'df' with columns 'file_path' and 'key'

# Sort the DataFrame by the 'key' column
df_sorted = df.sort_values('key')

# Group file paths by key
groups = groupby(df_sorted.iterrows(), key=lambda x: x[1]['key'])

# Specify the destination folder for the zip files
destination_folder = '/path/to/destination/folder/'

# Iterate over the groups and create zip files
for key, group in groups:
    file_paths = [row[1]['file_path'] for _, row in group]
    zip_file_path = os.path.join(destination_folder, f'{key}.zip')
    os.makedirs(destination_folder, exist_ok=True)
    with shutil.ZipFile(zip_file_path, 'w') as zip_file:
        for file_path in file_paths:
            zip_file.write(file_path, os.path.basename(file_path))