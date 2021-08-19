import pandas as pd
file= pd.read_excel('IMVA.xls')
print(file)

files=file['Period'].str.split(' ',n=1,expand=True)
print(files)

file= file.assign(year=files[1])

file.index=file['year']
print(file.index)

set1=file[(file['year'] >=str(2008)) & (file['year'] <= str(2017))]
print(set1)