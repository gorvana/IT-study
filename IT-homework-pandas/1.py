import pandas as pd

data = pd.read_csv('titanic.csv')

print(data['PassengerId'].count())
print(data['Age'].isna().sum())