# Here, we're importing the specific class Imputer from the library sklearn
from sklearn.impute import SimpleImputer
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

# Output
#       A     B     C    D
# 0   1.0   2.0   3.0  4.0
# 1   5.0   6.0   NaN  8.0
# 2  10.0  11.0  12.0  NaN

# Replace the missing values in each row with the column average
imr = SimpleImputer()
imr = imr.fit(data_frame.values)
imputed_data = imr.transform(data_frame.values)
print(imputed_data)

# Output
# [[ 1.   2.   3.   4. ]
#  [ 5.   6.   7.5  8. ]
#  [10.  11.  12.   6. ]]