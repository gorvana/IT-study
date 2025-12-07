import pandas as pd

data = pd.read_csv('titanic.csv')

print(data[data['Pclass']==1].Fare.mean())
print(((data['Pclass']==3) & (data['Survived']==1)).sum() / (data['Pclass']==3).sum())