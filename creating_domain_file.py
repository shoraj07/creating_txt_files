import os
import csv

def fetch_txt_files(directory_path):
    # Using list comprehension for brevity and ensuring unique file names
    return [file_name for file_name in os.listdir(directory_path) if file_name.endswith('.txt')]

def extract_elements(file_names):
    extracted_elements = []
    for file_name in file_names:
        parts = file_name.split('_')
        if len(parts) > 7:  # Ensure there are enough parts
            first_element = parts[0]
            second_element = parts[1].upper()
            fourth_element = parts[3].upper()
            seventh_element = parts[6]
            extracted_elements.append((first_element, second_element, fourth_element, seventh_element))
    return extracted_elements

def create_directory_structure(base_path, elements):
    for element_tuple in elements:
        path = os.path.join(base_path, element_tuple[0], element_tuple[1], element_tuple[2], element_tuple[3], 'CDR')
        os.makedirs(path, exist_ok=True)
        print("Created directory:", path)

def save_to_csv(file_path, data):
    header = ['first_element', 'second_element', 'fourth_element', 'seventh_element']
    with open(file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        csvwriter.writerows(data)
    print("Data saved to CSV file:", file_path)

if __name__ == '__main__':
    folder_path = 'txtFiles'  # Path to the directory containing the .txt files
    base_output_path = 'destFolders'  # Base path where the directories will be created
    csv_output_path = 'extracted_columns.csv'  # Path to save the CSV file

    txt_file_names = fetch_txt_files(folder_path)
    print("Text files found:", txt_file_names)
    
    extracted_data = extract_elements(txt_file_names)
    for data in extracted_data:
        print(data)
    
    create_directory_structure(base_output_path, extracted_data)
    save_to_csv(csv_output_path, extracted_data)
