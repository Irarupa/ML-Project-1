def extract_data_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read lines one by one
        lines = file.readlines()
    
    data = []
    for line in lines:
        # Split each line by a delimiter (example: '-')
        parts = line.strip().split('-')
        parts = [part.strip() for part in parts]  # clean whitespace
        data.append(parts)
    return data

# Usage
file_path = 'file.txt'
extracted_data = extract_data_from_file(file_path)
for entry in extracted_data:
    print(entry)