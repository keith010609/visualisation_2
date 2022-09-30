import pandas as pd

ma = pd.read_csv("data/Median age.csv")
le = pd.read_csv("data/Life expectancy.csv")
maL = ma['Country'].to_list()
# print(ma['Country'].head())
# print(leL)
le = le[le['Country'].isin(maL)].set_index('Country')
le.to_csv('test.csv')

