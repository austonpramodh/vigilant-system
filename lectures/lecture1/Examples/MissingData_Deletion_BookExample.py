import pandas as pd
import io

csv_data = \
    '''A,B,C,D
    1.0,2.0,3.0,4.0
    5.0,6.0,,8.0
    10.0,11.0,12.0,
    '''
data_frame = pd.read_csv(io.StringIO(csv_data))
print(data_frame)
print()

# Find the number of missing values per column
missing_values_per_column = data_frame.isnull().sum()
print(missing_values_per_column)
print()

# Drop all rows with missing data
print(data_frame.dropna(axis=0))
print()

# Drop all columns with missing data
print(data_frame.dropna(axis=1))
print()

# Drop all row with less than 4 values
print(data_frame.dropna(thresh=4))
print()

# Only drop rows where the value for column "C" is "NaN" (Not a Number)
print(data_frame.dropna(subset=['C']))
print()