from pandas_datareader import wb
data = wb.download(indicator='FP.CPI.TOTL.ZG', country='SG', start=1961, end=2020)
data = data.reset_index()
del data['country']
data.columns = ['year','inflation']
data = data.set_index('year')
data.to_csv('singapore.csv')
del data

world = wb.download(indicator='FP.CPI.TOTL.ZG', country='all', start=1961, end=2020).reset_index()
world.columns = ['country','year','inflation']
world = world.sort_values(by='year')
world.to_csv('world.csv')
del world