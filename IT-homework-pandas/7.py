import pandas as pd

data = pd.read_csv('titanic.csv')

print(data[data['Survived']==1].Age.mean())
print(data[data['Survived']==0].Age.mean())