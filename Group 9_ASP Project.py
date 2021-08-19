import pandas as pd
data = pd.read_excel('IMVA.xls',sheet_name="IMVA")
print(data)

files = data['Periods'].str.split(' ',n=1,expand=True)
print(files)

data = data.assign(year=data[1])

data.index = data['year']
print(data.index)

set1= data[(data['year'] >=str(2008)) & (data['year'] <= str(2017))]
print(set1)