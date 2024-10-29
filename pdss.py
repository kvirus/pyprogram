import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)


file = '123.csv'
df = pd.read_csv(file)

num = 4
file = R'c:\intel\111.txt'
# x = len(df)
# print(x)
columns = ['Email', 'Domain', 'Password']
columns1 = ['Password']
len = len(df)
outputxls= R'c:\intel\111.xls'
i = 0
xls_df = df[columns]
#xls_df.to_excel(outputxls)
while i < 700:
    with open(file,'w') as fil:
        x = str(df[columns].head(i))
        x1 = str(df.loc[i,'Password'])
        x2 = x1.isdigit()
        if x2:
            print(x)
            fil.write(x)
    i+=1
