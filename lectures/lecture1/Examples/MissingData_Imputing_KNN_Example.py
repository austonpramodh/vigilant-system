# Here, we're importing the specific class Imputer from the library sklearn
from sklearn.impute import KNNImputer
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

data_frame.filter

# Output
#       A     B     C    D
# 0   1.0   2.0   3.0  4.0
# 1   5.0   6.0   NaN  8.0
# 2  10.0  11.0  12.0  NaN

# Replace the missing values in each row with a -1

# I specify the nearest neighbor to be 3 
fea_transformer = KNNImputer(n_neighbors=3)
new_data_frame = fea_transformer.fit_transform(data_frame)
new_data_frame = pd.DataFrame(new_data_frame)
print(new_data_frame)
# Output
#       0     1     2    3
# 0   1.0   2.0   3.0  4.0
# 1   5.0   6.0   7.5  8.0
# 2  10.0  11.0  12.0  6.0

