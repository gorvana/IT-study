import pandas as pd

data = pd.read_csv('titanic.csv')

data['FamilySize'] = data['SibSp'] + data['Parch'] + 1

print(data[data['PassengerId']==889]['FamilySize'])