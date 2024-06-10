import os
from multiprocessing import Pool
import time

# Read file names from a text file and store them in a list
def read_file_names(file_path):
    with open(file_path, 'r') as file:
        file_names = [line.strip().replace("/", "_") + ".txt" for line in file if line.strip()]
    return file_names

# Content to be written to each file
file_content = "This is the content for the file.\n"

# Directory to save files
output_dir = "txtFiles"
os.makedirs(output_dir, exist_ok=True)

# Function to create a file and write content to it
def create_file(file_name):
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, 'w') as file:
        file.write(file_name)

# Number of processes to use
num_processes = 2

# Main block to create files using multiprocessing and measure execution time
if __name__ == '__main__':
    file_path = 'input/domain_file.txt'  # Path to the text file containing the file names
    file_names = read_file_names(file_path)

    start_time = time.time()  # Record the start time

    pool = Pool(processes=num_processes)
    pool.map(create_file, file_names)
    pool.close()
    pool.join()

    end_time = time.time()  # Record the end time

    print("Files have been created successfully.")
    print("Time taken: {:.2f} seconds".format(end_time - start_time))
