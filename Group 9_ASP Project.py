import pandas as pd

dataframe = None
with pd.ExcelFile("IMVA.xls") as reader:
    dataframe = pd.read_excel(reader, sheet_name='IMVA', usecols="A,AM:AZ")
print(dataframe)




