import multiprocessing

def worker():
    result_df = ...  # Process your DataFrame and get the result_df
    return result_df

num_processes = 3

if __name__ == '__main__':
    Processes = [multiprocessing.Process(target=worker) for _ in range(num_processes)]

    results = []  # To store the returned DataFrames

    for process in Processes:
        process.start()

    for process in Processes:
        process.join()
        result = process._target(*process._args, **process._kwargs)  # Get the return value
        results.append(result)

    # Now you have a list of DataFrames returned by each process
    print("Results:", results)