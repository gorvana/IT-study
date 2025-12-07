import pandas as pd

data = pd.read_csv('titanic.csv')

print(((data['Sex']=='female') & (data['Survived']==1) & (data['Pclass']==1)).sum())
print(((data['Age']<18) & (data['Parch']==0)).sum())