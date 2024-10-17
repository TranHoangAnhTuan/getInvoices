import json
import pandas as pd

# Load your JSON file
def save_to_excel(input_path, output_path):
    

    # Fields to extract
    fields = [
        'nbmst', 'khhdon', 'shdon', 'cqt', 'hdon', 'mhdon', 'mtdtchieu', 
        'nbdchi', 'nbten', 'nmdchi', 'nmten', 'tgtcthue', 'tgtthue', 'tgtttbso',
        'tlhdon', 'mkhang', 'nbsdthoai', 'msttcgp', 'hdhhdvu', 'tlhdon'
    ]

    # Fields within the 'thttltsuat' nested dictionaries (inside the list)
    nested_fields = ['tsuat', 'thtien', 'tthue']

    # Open and load the JSON file
    with open(input_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Prepare a list to hold all rows of data
    all_rows = []

    # Iterate through each dictionary in "datas"
    for entry in data.get('datas', []):
        # Extract main fields
        row = {field: entry.get(field, '') for field in fields}
        
        # Handle 'thttltsuat', which is expected to be a list of dictionaries
        thttltsuat_list = entry.get('thttltsuat', [])
        if isinstance(thttltsuat_list, list):
            for thttltsuat in thttltsuat_list:
                # Create a copy of the row for each 'thttltsuat' entry
                row_copy = row.copy()
                # Extract the fields from each item in 'thttltsuat'
                for nf in nested_fields:
                    row_copy[f'thttltsuat[{nf}]'] = thttltsuat.get(nf, '')
                # Add the row to the list of all rows
                all_rows.append(row_copy)
        else:
            # Handle case where 'thttltsuat' is not a list (fill with empty values)
            for nf in nested_fields:
                row[f'thttltsuat[{nf}]'] = ''
            all_rows.append(row)

    # Convert the list of rows to a pandas DataFrame
    df = pd.DataFrame(all_rows)

    # Save DataFrame to an Excel file
    df.to_excel(output_path, index=False)

    print(f"Data has been extracted and saved to {output_path}")
