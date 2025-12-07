import pandas as pd

data = pd.read_csv('titanic.csv')

print((data['Sex']=='male').sum())
print((data['Pclass']==1).sum())