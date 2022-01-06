'''This file will create an extra column and extrat all 
the url to domain and add it that extra comlumn 
Created : 06.01.22
Author  : Khandoker Tanjim Ahammad


'''

import pandas as pd
fileinput = str(input("Type .csv file name:"))
df = pd.read_csv(fileinput)
df[str(input("Name the new column with domain: "))]=df[str(input("Columm name with url: "))].str.extract('//(www\.){0,1}(.*?)/')[1]
print(df.head(2))
df.to_csv(fileinput)