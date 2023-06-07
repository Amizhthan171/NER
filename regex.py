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

    # Combine all CSV files into a single DataFrame
    combined_df = pd.concat([pd.read_csv(os.path.join(directory, csv_file)) for csv_file in csv_files])

    # Drop the index column if present
    combined_df.reset_index(drop=True, inplace=True)

    # Convert the file path column to a list
    file_paths = combined_df['file_path'].tolist()

    # Determine the chunk size
    chunk_size = len(file_paths) // num_processes

    # Split the file paths into chunks
    chunks = [file_paths[i:i+chunk_size] for i in range(0, len(file_paths), chunk_size)]

    # Create a process pool
    with Pool(processes=num_processes) as pool:
        results = []

        # Process each chunk in parallel
        for chunk in chunks:
            chunk_results = pool.map(check_file_exists, chunk)
            results.extend(chunk_results)

    # Add the results as a new column in the combined DataFrame
    combined_df['Exists'] = results

    # Continue processing the combined DataFrame with the existence status