import os
from multiprocessing import Pool

def count_files(directory):
    file_count = 0
    for root, dirs, files in os.walk(directory):
        file_count += len(files)
    return file_count

if __name__ == '__main__':
    directory_path = '/path/to/directory'  # Replace with the actual directory path
    pool = Pool(processes=os.cpu_count())
    result = pool.apply_async(count_files, (directory_path,))
    file_count = result.get()
    print("Number of files:", file_count)