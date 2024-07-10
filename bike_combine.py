import pandas as pd
import os

# Directory containing the CSV files
dir_path = r'C:\Users\roen\Desktop\Google Project\Bike Project\original_csv_db'

# List of CSV files to combine
csv_files = [
    f'202201-divvy-tripdata.csv',
    f'202202-divvy-tripdata.csv',
    f'202203-divvy-tripdata.csv',
    f'202204-divvy-tripdata.csv',
    f'202205-divvy-tripdata.csv',
    f'202206-divvy-tripdata.csv',
    f'202207-divvy-tripdata.csv',
    f'202208-divvy-tripdata.csv',
    f'202209-divvy-tripdata.csv',
    f'202210-divvy-tripdata.csv',
    f'202211-divvy-tripdata.csv',
    f'202212-divvy-tripdata.csv'
]

# Initialize an empty list to hold dataframes
dfs = []

# Iterate over the list of files and read them into dataframes
for csv_file in csv_files:
    file_path = os.path.join(dir_path, csv_file)
    df = pd.read_csv(file_path)
    dfs.append(df)
    print(f'{csv_file} has {len(df)} rows.')

# Concatenate all dataframes into one
combined_df = pd.concat(dfs, ignore_index=True)

# Save the combined dataframe to a new CSV file
combined_csv_path = os.path.join(dir_path, 'combined_divvy_tripdata.csv')
combined_df.to_csv(combined_csv_path, index=False)

# Report the row count of the combined dataframe
print(f'Combined dataset has {len(combined_df)} rows.')

# Report the operation is complete
print('Operation combine complete.')