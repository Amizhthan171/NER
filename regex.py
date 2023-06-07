import pandas as pd
import os
from multiprocessing import Pool

# Function to check file existence
def check_file_exists(file_path):
    return os.path.exists(file_path)

# Process a single row
def process_row(row):
    file_path = row['FilePath']
    exists = check_file_exists(file_path)
    return exists

# Main function
if __name__ == '__main__':
    # Read the CSV file
    df = pd.read_csv('your_file.csv')

    # Number of processes to utilize
    num_processes = 4

    # Split the DataFrame into chunks
    chunks = np.array_split(df, num_processes)

    # Create a process pool
    pool = Pool(processes=num_processes)

    # Process each chunk in parallel
    results = pool.map(process_row, chunks)

    # Concatenate the results
    df['Exists'] = pd.concat(results)

    # Continue processing the dataframe with the existence status