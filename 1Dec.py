import pandas as pd
#importing data
df = pd.read_csv('nobel.csv',delimiter=',') #by default delimiter is cooma.
# df = pd.read_excel('titanic.xlsx')
#Filtering DATA
#column wise filtering
# print(df['year'])
# print(df[['year','category']]) #for two columns we passed as a list and get what we want.
# print(df[df['year'] == 1901]) #filtering data by year

#row wise filtering
# print(df['sex']=='Male') #give ture and false 
# print(df[df['sex']=='Male']) #give the data of true for 'Male'
# print(df[df['sex']=='Female']) #give the data of true for 'Female'
# print(df[df['sex']=='Female'].head()) #give the head data like start 5,6 rows of true for 'Female'
# print(df[df['year']<=1950]) #till 1950's
#to get noble prinze winners from 1920 to 1950
# print(df[(df['year']<=1920) & (df['year']>=1950)]) #and is logical operator
# print(df[(df['category']=='Chemistry') | (df['category']=='Physics')]) #Learn about OR | this is or operator symbol.
#explore OR operator and all about and,or operators at HOME.
# print(df.columns)
# print(df[(df['category']=='Physics') | ((df['category']=='Physics') & (df['category']=='Chemistry'))]) #use or,and in a single line.

#see the btwn funciton
# print(df[df['year'].between(1920,1950)])
#Learn loc funtion and Iloc function is used to filer rows with help of rows
# print(df.loc[10:24])
# print(df.loc[10:15,['sex']]) #last index included ok , label(col name) given for speciic column
# print(df.iloc[10:15,1:5]) #particular data of specifc row and column , use iLoc.
#Learn value count
# print(df.sex.value_counts())
# print(df.category.unique())#check unique value in a column. like here we do for caterogy column.
# print(df.category.nunique()) #num of unique values.
# print(type(df.category.unique())) #checking type
# print(type(df.category.tolist())) #convert anytype of data into List.
#Learn about Aggregate functions
# print(df.year.sum())
#i'm usig titanic dataset ok.
# print(df.columns) 
# print(df.survived.sum())

# print(df.age.mean())
# print(df.age.mode())
# print(df.age.median())
# print(df.age.std())

#ok now us nobel dataset
# print(df.isnull)
# print(df.isna().sum().sort_values(ascending=False))
print(df.copy(deep='False'))
