import os
import pandas as pd

folder_path = '/Users/andrewweddell/extract/archive'  # Adjust the path to your needs

csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
print(f"List of CSV files: {csv_files}")  # Print the list of CSV files

dfs = []  # List to hold the individual DataFrames

for file in csv_files:
    file_path = os.path.join(folder_path, file)
    try:
        data = pd.read_csv(file_path, error_bad_lines=False)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        continue
    
    if data.empty:
        print(f"{file} is empty. Skipping...")  # Print if the current CSV file is empty
        continue
    
    print(f"Appending data from {file}")  # Print the name of the current CSV file being appended
    print(data.head())  # Print the first few rows of the current CSV file
    
    dfs.append(data)  # Append the DataFrame to the list

# Concatenate all the DataFrames in the list to create the merged DataFrame
merged_data = pd.concat(dfs, ignore_index=True)

print("Merged Data:")  # Print the final merged DataFrame
print(merged_data.head())  # Print the first few rows of the merged DataFrame

if not merged_data.empty:
    merged_data.to_csv(os.path.join(folder_path, 'merged_file.csv'), index=False)
else:
    print("Merged DataFrame is empty. No file was saved.")
