import pandas as pd

data = pd.read_csv('winemag-data-130k-v2.csv')

print(data.isna().sum())