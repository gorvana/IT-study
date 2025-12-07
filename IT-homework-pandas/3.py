import pandas as pd

data = pd.read_csv('titanic.csv')

print((data['Survived']==1).sum())
print((data['Survived']==1).sum()/data['Survived'].count()*100)

print(((data['Survived']==1) & (data['Sex']=='female')).sum()/(data['Sex']=='female').sum()*100)
print(((data['Survived']==1) & (data['Sex']=='male')).sum()/(data['Sex']=='male').sum()*100)