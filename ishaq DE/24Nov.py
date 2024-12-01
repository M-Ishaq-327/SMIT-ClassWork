import pandas as pd
#importing data
df = pd.read_csv('nobel.csv',delimiter=',') #by default delimiter is cooma.
# df = pd.read_excel('titanic.xlsx')
# df = pd.read_csv(r'C:\Users\smit\Downloads\jo.tsv',delimiter='\t') # i dont add file and using path giving method.
print(df.head())
#last 5 rows
print(df.tail())
print(df.tail(7)) #print last 7 rows

#checking dataset:
print(df.shape)
#checking number of rows and columns
print(df.shape[0])
#columns names
print(df.columns)
