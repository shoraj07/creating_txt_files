import os
from multiprocessing import Pool
import time

# Generate a list of file names
file_count = 4000  # For example, 100 files
file_names = ["file_{0}.txt".format(i) for i in range(file_count)]

# Content to be written to each file
file_content = "This is the content for the file.\n"

# Directory to save files
output_dir = "txtFiles"
os.makedirs(output_dir, exist_ok=True)

# Function to create a file and write content to it
def create_file(file_name):
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, 'w') as file:
        file.write(file_content)

# Number of processes to use
num_processes = 10

# Main block to create files using multiprocessing and measure execution time
if __name__ == '__main__':
    start_time = time.time()  # Record the start time

    pool = Pool(processes=num_processes)
    pool.map(create_file, file_names)
    pool.close()
    pool.join()

    end_time = time.time()  # Record the end time

    print("Files have been created successfully.")
    print("Time taken: {:.2f} seconds".format(end_time - start_time))
