import pandas as pd
import os
from multiprocessing import Pool

# Function to check file existence
def check_file_exists(file_path):
    return os.path.exists(file_path)

# Main function
if __name__ == '__main__':
    # Directory containing the CSV files
    directory = 'path/to/your/csv/directory'

    # Get the list of CSV files in the directory
    csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

    # Number of processes to utilize
    num_processes = 4

    # Create a process pool
    with Pool(processes=num_processes) as pool:
        results = []

        for csv_file in csv_files:
            # Construct the full path to each CSV file
            file_path = os.path.join(directory, csv_file)

            # Read the CSV file
            df = pd.read_csv(file_path)

            # Process each row in parallel
            chunk_results = pool.map(check_file_exists, df['file_path'])
            results.extend(chunk_results)

        # Continue processing the results