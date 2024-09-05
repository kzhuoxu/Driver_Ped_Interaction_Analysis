import os
import pandas as pd

# Specify the path to your 'xcped' folder
folder_path = os.path.expanduser('~/Desktop/xcped')

# List to store the extracted data
extracted_data = []

# Traverse through the folder
for root, dirs, files in os.walk(folder_path):
    # Look for folders labeled 'QN_csv'
    if 'QN_csv' in root:
        # Go through each file in the 'QN_csv' folder
        for file in files:
            # Check if the file contains '105' in the title and is a CSV file
            if '105' in file and file.endswith('.csv'):
                file_path = os.path.join(root, file)
                # Read the specific columns from the CSV file
                df = pd.read_csv(file_path, usecols=['H', 'L'])
                # Append the data to the list
                extracted_data.append(df)

# Concatenate all the data into a single DataFrame
final_data = pd.concat(extracted_data, ignore_index=True)

# Display or save the final DataFrame
print(final_data)

# Save the data to a new CSV file:
final_data.to_csv(os.path.expanduser('~/Desktop/xcped/extracted_H_L_columns.csv'), index=False)
